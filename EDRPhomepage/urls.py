from django.urls import path
from . import views

urlpatterns = [
    path('', views.getdata, name="data"),
    path('updatedata/<str:pk>/', views.updatedata, name="updatedata")
]
