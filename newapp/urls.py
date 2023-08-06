from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage),
    path('addnew/', views.addnew),
    path('test/', views.test),
]