from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("", views.index, name='home'),
    path("reviews", views.reviews, name='reviews'),
    path("contact", views.Contact, name='Contact'),
    path("myteam", views.myteam, name='myteam'),
    path("logIn", views.logIn, name='logIn'),
    path("logInsignup", views.logInsignup, name="logInsignup"),
    path("product/logInsignup", views.logInsignup, name="logInsignup"),
    path("product", views.product, name = "product"), 
    path("sign-in", views.sign_in, name='sign_in'),
    path("product/login-page2", views.login_page2, name = "login-page2")
]

