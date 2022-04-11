from models import Emprunt
from django.db.models import Sum

tati=  Emprunt.objects.values('nom', 'date__month').orderby('date').annotate(total=sum('montant'))
print(tati)