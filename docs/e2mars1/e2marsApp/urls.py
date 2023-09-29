from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home),
    path("DashBoard", views.DashBoard),
    path("Restaurant", views.OrderFood),
    path("Repair", views.Repair),
    path("FindItems", views.Transportation),
    path("Selling", views.Selling),
    path("ProductUpload", views.Product),
    path("LogIn", views.LogIn),
    path("Register", views.Register)
]
