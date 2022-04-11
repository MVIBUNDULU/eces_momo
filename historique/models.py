from calendar import month
from django.db import models

# Create your models here.

class Creditation(models.Model):
    date=models.DateField()
    sold_actuel=models.IntegerField()
    derniere_creditation=models.IntegerField()
#pour preciser l'élément à affichicher dans la page admin
    def __str__(self):

        return f"Sold actuel :{self.sold_actuel} / Dernier creditation {self.derniere_creditation} /  Mois:   {self.date}"

class Emprunt(models.Model):
    date=models.DateField()
    nom=models.CharField(max_length=100)
    montant=models.IntegerField()
    numero=models.CharField(max_length=9)

    def __str__(self):

        return f"Nom :{self.nom} /  le montant {self.montant} /  Mois:   {self.date}"


class Paiement(models.Model):
    date=models.DateField()
    numero=models.CharField(max_length=9)
    montant=models.IntegerField()

    def __str__(self):

        return f"Numéro :{self.numero} / le montant {self.montant}  / Mois: {self.date}"


class Envoie(models.Model):
    date=models.DateField()
    nom=models.CharField(max_length=100)
    montant=models.IntegerField()
    numero=models.CharField(max_length=9)

    def __str__(self):

        return f"Nom :{self.nom} / le montant {self.montant} /  Mois:   {self.date}"



