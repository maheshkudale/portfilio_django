from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('about',views.about,name='about'),
    path('project',views.project,name='project'),
    path('contact',views.contact,name='contact'),
    
]