"""search_operation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path as urlPath
from search.views import search_papers, delete_objects, view_paperdb
from researcher.views import register, login, logout
from researcher.views import update

contextPath = 'scholar-hub/'

def pathWithContext(path, pattern):
    return urlPath(contextPath + path, pattern)

urlpatterns = [
    pathWithContext('user', register),
    pathWithContext('user/login', login),
    pathWithContext('user/logout', logout),
    pathWithContext('user/update', update),
    urlPath('paper/search/input=<str:keywords>&<int:number>', search_papers),
    urlPath('paper/search/delete_all_objects', delete_objects),
    urlPath('paper/search/test/show_paper_db', view_paperdb)
]
