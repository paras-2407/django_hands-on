from django.urls import path
from . import views #. signifies that import views from the current directory


urlpatterns=[
    path("", views.index, name="index-page"), #http url, function index from file views, name refers to the urls in the whole project
    path("home/", views.home, name="home-page"), #http url, function index from file views, name refers to the urls in the whole project
    path("about/", views.about, name="about-page"),
    path("contact/",views.contact, name='contact-page'),
    path('login/', views.login, name='login-form'),
    path('services/', views.services, name='services-provided'),
    path('new_index/', views.new_index, name='new_index-page')
]