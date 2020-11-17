"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from . import views

""" path( la url propiamente dicha, la vista , un nombre para url) """

urlpatterns = [
    path('index/', views.index, name='index'),
    path('lista/', views.lista, name='lista'),
    path('lista2/', views.lista2, name='lista2'),
    path('lista3/', views.lista3, name='lista3'),
    path('lista4/', views.lista4, name='lista4'),
    path('lista5/', views.lista5, name='lista5'),
    path('lista6/', views.lista6, name='lista6'),
    path('parametros/<str:name>' , views.parametros, name='parametros')

]
