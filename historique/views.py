from datetime import date
from distutils.log import error
from itertools import count
from django.shortcuts import redirect, render
#from models import Creditation, Emprunt, Envoie, Paiement
#la deconnexion
from django.contrib.auth import authenticate, logout,login as dj_login
#après deconnexion faudrait se reloguer pour utiliser l appli
from django.contrib.auth.decorators import login_required
#from django.shortcuts import
#message erreur
from django.contrib import messages
#importation model de la création compte register
from django.contrib.auth.models import User
from historique.models import Emprunt,Envoie,Paiement,Creditation
from django.db.models import Sum


def deconnexion(request):
    logout(request)
    return redirect("login")
# Create your views here.

@login_required
def Home(request):
#dictionnaire recuperant le nombre d'element des differentes tables
    data={"totalenvoie":Envoie.objects.all().count(),
    "totalcreditation":Creditation.objects.all().count(),
    "totalemprunt":Emprunt.objects.all().count(),
    "totalpaiement":Paiement.objects.all().count(),
    }
    return render(request, 'pages/home.html',data)

       

@login_required
def paiement(request):
    if request.POST:
        data=request.POST
        paiementInstance=Paiement.objects.create(
        date=data.get("date"),
        numero=data.get("numero"),
        montant=data.get("montant"),
        )


    return render(request, 'pages/formulaire/paiement.html')
#Les controlleurs des formulaires + validation des données

@login_required
def emprunt(request):

    if request.POST:
        data=request.POST
        empruntInstance=Emprunt.objects.create(
            date=data.get("date"),
            nom=data.get("nom"),
            numero=data.get('numero'),
            montant=data.get("montant"),
        )

    return render(request, 'pages/formulaire/emprunt.html')

#fontion de création de compte

@login_required    
def creercompte(request):
    if request.POST:
        data=request.POST
        if data.get('pwd')==data.get('pwd1'):
            creercompteInstance=User.objects.create_user(
            username=data.get("username"),
            password=data.get("pwd"),
              )
            
            messages.success(request, "Compte créé avec succès")
        
        else:
            messages.error(request,"Les deux mots de passes ne correspndent pas")
           
      
   
    return render(request,'pages/parametre/compte.html')

@login_required
def envoie(request):

    if request.POST:
        data=request.POST
        envoieInstance=Envoie.objects.create(

                date=data.get("date"),
                nom=data["nom"],
                numero=data.get("numero"),
                montant=data.get("montant"),
           
        )

    return render(request, 'pages/formulaire/envoie.html')

@login_required
def creditation(request):

    if request.POST:
        data=request.POST
        creditationInstance=Creditation.objects.create(

            date=data.get("date"),
            sold_actuel=data.get("sold_actuel"),
            derniere_creditation=data.get("derniere_creditation"),
        )

    return render(request, 'pages/formulaire/creditation.html') 

def login(request):
    if request.POST:
        data=request.POST
        print(data)
        user=authenticate(request,username=data.get("username"), password=data.get("password"))
        print(user)
        if user is not None:
            dj_login(request,user)
            return redirect("home")
        messages.error(request,"Les informations sont incorrectes")
    return render(request, 'pages/formulaire/login.html')

    
    
@login_required
def tablecreditation(request):
#requete select * from Creditation, 
# db_creditation est la valeur renommée de data qui sera utilisée sur le template    
    data={"db_creditation":Creditation.objects.all()}
    return  render(request,'pages/tables/tablecreditation.html',data)

@login_required
def tableenvoie(request):
    #requete select * from Envoie, 
# db_envoie est la valeur renommée de data qui sera utilisée sur le template
    data={"db_envoie":Envoie.objects.all()}
    return  render(request,'pages/tables/tableenvoie.html',data) 

@login_required
def tableemprunt(request):
        #requete select * from Emprunt, 
# db_emprunt est la valeur renommée de data qui sera utilisée sur le template
    data={"db_emprunt":Emprunt.objects.all().order_by('-id') }
    #etatemprunt={"resultatemprunt": Emprunt.objects.values('nom', 'date__month').order_by('date__month').annotate(total=Sum('montant'))}
    #print(etatemprunt)
   # totalemprunt1={"totalemprunt":Emprunt.objects.values('montant').annotate(Sum('montant'))}
   # print(totalemprunt1)
    return  render(request,'pages/tables/tableemprunt.html',data)

@login_required
def tablepaiement(request):
        #requete select * from Paiement, 
# db_paiement est la valeur renommée de data qui sera utilisée sur le template
    data={"db_paiement":Paiement.objects.all()}
    return  render(request,'pages/tables/tablepaiement.html',data) 


@login_required
def etatemprunt(request):
        #requete select * from Emprunt, 
# db_emprunt est la valeur renommée de data qui sera utilisée sur le template
    #data={"db_emprunt":Emprunt.objects.all()}
    etatemprunt={"resultatemprunt": Emprunt.objects.values('nom','date__month').order_by('date__month').annotate(total=Sum('montant'))}
    #print(etatemprunt)
    #date={"mois1":1, "mois2":2, "mois3":3, "mois4":4, "mois5":5, "mois6":6, "mois7":7, "mois8":8, "mois9":9, "mois10":10, "mois11":11, "mois12":12}

    return  render(request,'pages/tables/etatemprunt.html',etatemprunt)

 #etat creditation
@login_required
def etatcreditation(request):
    data={"etat_creditation":Creditation.objects.values('date__month',).order_by('date__month').annotate(total=Sum('sold_actuel'))}
    print(data)
    return render(request,'pages/tables/etatcreditation.html',data)  

#etat envoie par jour
@login_required
def etatenvoiejour(request):
    data={"etat_envoie_jour":Envoie.objects.values('date__month','nom').order_by('date__month').annotate(total=Sum('montant'))}
    print(data)
    return render(request,'pages/tables/etatenvoiejour.html',data) 


#etat paiement par mois
@login_required
def etatpaiement(request):
    data={"etat_paiement_mois":Paiement.objects.values('date__month','numero').order_by('date__month').annotate(total=Sum('montant'))}
    print(data)
    return render(request,'pages/tables/etatpaiement.html',data)        

    
