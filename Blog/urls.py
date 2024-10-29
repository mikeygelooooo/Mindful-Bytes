from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("post/<str:slug>/", views.full_post, name="full_post"),
]
