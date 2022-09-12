from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', views.home,name="home"),
    path('predict', views.predict,name="predict"),

   
]
urlpatterns += staticfiles_urlpatterns()