"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.http import HttpResponse
from historique import views


def Contact(requet):
    return HttpResponse("Hello")

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('contact/',Contact ),
    path('home/',views.Home,name='home'),
    path('paiement/', views.paiement,name='paiement'),
    path('envoie/', views.envoie,name='envoie'),
    path('emprunt/', views.emprunt,name='emprunt'),
    path('creditation/', views.creditation,name='creditation'),
    path('creercompte/', views.creercompte,name='compte'),
    #la connexion
    path('login/', views.login,name='login'),
    #deconnexion
     path('deconnexion/', views.deconnexion,name='deconnexion'),

    #URL pour des tables
    path('tablecreditation/', views.tablecreditation,name='tablecreditation'),
    path('tableenvoie/', views.tableenvoie,name='tableenvoie'),
    path('tableemprunt/', views.tableemprunt,name='tableemprunt'),
    path('tablepaiement/', views.tablepaiement,name='tablepaiement'),

    #URL des etats

    path('etatemprunt/', views.etatemprunt,name='etatemprunt'),
    path('etatcreditation/', views.etatcreditation,name='etatcreditation'),
    path('etatenvoiejour/', views.etatenvoiejour,name='etatenvoiejour'),
    path('etatpaiement/', views.etatpaiement,name='etatpaiement')

]


