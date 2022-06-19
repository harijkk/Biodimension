from django.urls import path
from . import views

urlpatterns = [
    path('', views.index1, name="home"),
    path('products/bioDcornea', views.bioDcornea, name="bioDcornea"),
    path('products/bioDvaginal', views.bioDvaginal, name="bioDvaginal"),
    path('products/bioDskin', views.bioDskin, name="bioDskin"),
    path('about', views.about, name="about"),
    path('join', views.join, name="join"),
    path('contact', views.contact, name="contact"),
    path('send_mail', views.send1, name="send_mail"),
    path('send_mail_attach', views.send_attach, name="send_mail_attach"),

]
