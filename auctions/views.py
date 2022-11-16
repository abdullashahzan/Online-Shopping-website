from urllib.request import HTTPRedirectHandler
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from auctions.models import auction, watchlist, bid, comment

from .models import User

def index(request):
    a = auction.objects.all()
    for i in a:
        if str(i.winner) == str(request.user):
            return render(request, "auctions/index.html", {
                "data": auction.objects.all(),
                "u": str(request.user)
            })
    return render(request, "auctions/index.html", {
        "data": auction.objects.filter(oc= True),
        "u": str(request.user)
    })

def deletelisting(request):
    if request.method == "POST":
        title = str(request.POST['listooo'])
        a = auction.objects.get(title= title)
        a.delete()
    return HttpResponseRedirect(reverse("index"))

def redirectAuction(request):
    return render(request, "auctions/auctionPage.html")

def getlisting(request):
    if request.method == "POST":
        title = request.POST['title']
        des = request.POST['desc']
        sbid = request.POST['bid']
        iurl = request.POST['img']
        cat = request.POST['category']
        if title != "" and des != "" and sbid != "":
            current_user = request.user
            data = auction(user= current_user, title= title, description= des, bid= sbid, url= iurl, category= cat)
            data.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/errorpage.html", {
                "code": 100  #mandatory fields not filled
            })

def listingdetails(request, listing):
    # for watchlist
    value = 61
    if watchlist.objects.filter(listing= listing, user= str(request.user)).exists():
        value = 60
    #to check if the user who clicked is the same person who posted
    current_user = str(request.user)
    posted_user = str(auction.objects.get(title=listing).user)
    if current_user == posted_user:
        user = 101
    else:
        user = 0
    com = comment.objects.filter(title= listing)
    return render(request, "auctions/listingPage.html", {
        "item": auction.objects.get(title= listing),
        "cuser": user,
        "value": value,
        "comments": com
    })

def fbid(request, listing):
    return render(request, "auctions/placebid.html", {
        "item": listing,
        "currentprice": float(auction.objects.get(title= listing).bid)
    })

def checkbid(request):
    if request.method == "POST":
        saidprice = float(request.POST['bidprice'])
        currentpr = float(request.POST['currentp'])
        item = str(request.POST['listoo'])
        userkun = str(auction.objects.get(title= item).user)
        if saidprice > currentpr:
            newbid = bid(user= str(request.user), bid= saidprice, item= item)
            newbid.save()
            newauctionprice = auction.objects.get(title= item, user= userkun)
            newauctionprice.bid = saidprice
            newauctionprice.save()
            return render(request, "auctions/errorpage.html", {
                "code": 97
            })
    return render(request, "auctions/errorpage.html", {
        "code": 56,
        "currentprice":currentpr
    })


def fwatchlist(request):
    if request.method == "POST":
        listing = "Clothes"
        if str(request.POST.get('listo')) == "add":
            listing = str(request.POST['addlisting'])
            watcher = watchlist(listing=listing, user= str(request.user))
            watcher.save()
        elif str(request.POST.get('listo')) == "remove":
            listing = str(request.POST['remlisting'])
            watchlist.objects.get(listing= listing, user= str(request.user)).delete()
        return HttpResponseRedirect(reverse("listingdetails", args=(listing,)))
    else:
        things = watchlist.objects.filter(user= str(request.user))
        l = []
        for i in things:
            title = i.listing
            thingsfromauction = auction.objects.get(title = title)
            imageurl = thingsfromauction.url
            despacito = thingsfromauction.description
            l.append([title, imageurl, despacito])
        return render(request, "auctions/watchlist.html", {
            "things": l
        })

def categories(request):
    c = auction.objects.all()
    l= []
    for i in c:
        if i.category not in l:
            l.append(i.category)
    return render(request, "auctions/categories.html", {
        "bruh": l
    })

def showcat(request, cat):
    ayo = auction.objects.filter(category= cat)
    return render(request, "auctions/showcategory.html", {
        "nani": ayo
    })

def fcomment(request):
    if request.method == "POST":
        name = str(request.POST['titlesama'])
    return render(request, "auctions/comment.html", {
        "title": name
    })

def post(request):
    if request.method == "POST":
        user = str(request.user)
        com = str(request.POST['comment'])
        item = str(request.POST['title'])
        head = str(request.POST['heading'])
        comment(user= user, comment= com, title= item, heading= head).save()
    return HttpResponseRedirect(reverse("listingdetails", args=(item,)))

def closeauc(request):
    if request.method == "POST":
        item = str(request.POST['title'])
        price = float(request.POST['price'])
        highestbidder = bid.objects.get(bid= price)
        a = auction.objects.get(title= item, bid= price)
        a.winner = highestbidder.user
        a.oc = False
        a.save()
    return render(request, "auctions/errorpage.html", {
        "code": 1,
        "price": price
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
