from django.contrib import admin
from historique.models import *

# Register your models here.
#enregistrement du model dans l'interface d'administration de django
admin.site.register(Creditation)
admin.site.register(Envoie)
admin.site.register(Emprunt)
admin.site.register(Paiement)

