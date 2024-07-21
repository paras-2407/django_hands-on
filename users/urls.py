from django.urls import path
from . import views #. signifies that import views from the current directory


urlpatterns=[
    path("register/", views.register, name="register-page"), #http url, function index from file views, name refers to the urls in the whole project
]