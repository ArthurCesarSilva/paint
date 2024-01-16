from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.curtidas, name="curtidas"),
    # website.com\red
    path("<str:color_name>/", views.colorpage)
   
]