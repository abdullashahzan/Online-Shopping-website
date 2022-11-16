from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    #This path directs user to auctionPage.html
    path("redirectAuctionPage", views.redirectAuction, name="auctionPage"),
    #Create Listing form submit button path
    path("getlisting", views.getlisting, name="getlisting"),
    #When a listing is clicked aka when redirected to listing page
    path("listing/<str:listing>", views.listingdetails, name="listingdetails"),
    #Placing a bid
    path("bid/<str:listing>", views.fbid, name="placebid"),
    #watchlist
    path("watchlist", views.fwatchlist, name="watchlist"),
    #check bid
    path("checkbid", views.checkbid, name='checkbid'),
    #categories
    path("categories", views.categories, name='categories'),
    path("showcat/<str:cat>", views.showcat, name='showcat'),
    #comment
    path("comment", views.fcomment, name='comment'),
    path("post", views.post, name="post"),
    #closing the auction
    path("closauc", views.closeauc, name="closeauc"),
    path("deletelisting", views.deletelisting, name="deletelisting")
 
]
