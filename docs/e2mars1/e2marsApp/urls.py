from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home),
    path("Home", views.Home),
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
    path("Team", views.Team),
    path("Taxi", views.Taxi),
    path('api/endpoint', views.chatbot_view, name='chatbot_view'),

]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

