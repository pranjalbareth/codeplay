"""devlogs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from blog import views


urlpatterns = [
		path('', views.home, name='home'),
		path('blog/', views.blog, name='blog'),
		path('resources/', views.resources, name='resources'),
        path('playground/', views.playground, name='playground'),
        path('events/', views.events, name='events'),
		path('blogpost/<str:slug>', views.blogpost, name='blog'),
        path('join/', views.join, name='join'),
        path('General/', views.blog, name='General'),
        path('projects/', views.projects, name='projects'),
        path('search/', views.search, name='search'),
        path('about/', views.about, name='about'),
        path('wizcode/', views.wizcode, name='wizcode')
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)