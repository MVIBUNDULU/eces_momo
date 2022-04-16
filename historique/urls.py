from django.urls import path
from django.http import HttpResponse
from historique import views


def Contact(requet):
    return HttpResponse("Hello")

urlpatterns = [
    #path('contact/',Contact ),
    path('home/',views.Home,name='home'),
    path('paiement/', views.paiement,name='paiement'),
    path('envoie/', views.envoie,name='envoie'),
    path('emprunt/', views.emprunt,name='emprunt'),
    path('creditation/', views.creditation,name='creditation'),
    path('creercompte/', views.creercompte,name='compte'),
    #la connexion
    path('', views.login,name='login'),
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


