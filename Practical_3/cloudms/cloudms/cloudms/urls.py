"""
URL configuration for cloudms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from messageapp import views as msgviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('msggate/', include('messageapp.urls')),
    path('tt/', msgviews.homeproc),
    path('tt1/', msgviews.homeproc1),
    path('tt2/', msgviews.homeproc2),
    path('tt3/', msgviews.homeproc3),
    path('tt4/', msgviews.homeproc4),
    path('tt5/', msgviews.homeproc5),
    path('tt6/', msgviews.homeproc6),
    #path('', msgviews.pgproc),
]   
