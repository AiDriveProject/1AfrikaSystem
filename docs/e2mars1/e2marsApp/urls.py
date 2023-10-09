from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home),
    path("DashBoard", views.DashBoard),
    path("Restaurant", views.OrderFood),
    path("Renting", views.Renting),
    path("Repair", views.Repair),
    path("FindItems", views.Transportation),
    path("Selling", views.Selling),
    path("ProductUpload", views.Product),
    path("LogIn", views.LogIn),
    path("Register", views.Register),
    path("Team", views.Team),
    path("Taxi", views.Taxi),
    path('api/endpoint', views.chatbot_view, name='chatbot_view'),
]

