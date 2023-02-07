# users/urls.py
from django.urls import path
from . import views
from .views import home ,SignUp

urlpatterns = [
    path('', home, name = "home"),
    #path('', views.upload_photo, name='home'),
    path("signup/", views.SignUp.as_view(), name="signup"),
    #path("upload_photo", views.upload_photo, name="upload_photo")
    #path("upload_success/", views.upload_success, name="upload_success")
]
