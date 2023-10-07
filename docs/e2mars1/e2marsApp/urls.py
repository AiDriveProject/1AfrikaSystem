from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home),
    path('dashboard/', views.DashBoard, name='DashBoard'),
    path("DashBoard", views.DashBoard, name='display_data'),
    path("Restaurant", views.OrderFood),
    path("Renting", views.Renting),
    path("Repair", views.Repair),
    path("FindItems", views.Transportation),
    path("Selling", views.Selling),
    path("ProductUpload", views.Product),
    path("LogIn", views.LogIn),
    path("Register", views.Register),
    path("Team", views.Team)
]

