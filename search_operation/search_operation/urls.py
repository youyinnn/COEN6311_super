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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from search.views import search_papers, delete_objects, view_paperdb

urlpatterns = [
    path('admin/', admin.site.urls),
    path('paper/search/input=<str:keywords>&<int:number>', search_papers),
    path('paper/search/delete_all_objects', delete_objects),
    path('paper/search/test/show_paper_db', view_paperdb)
]
