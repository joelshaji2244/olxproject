from django.urls import path
from olx_api import views
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register("vechile", views.VechicleViewSet, basename="vechile")

urlpatterns = [

    path('register/', views.UserCreationView.as_view()),
    
]+routers.urls