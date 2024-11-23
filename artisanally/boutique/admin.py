from django.contrib import admin
from boutique.models import Produit, Commande, Panier

admin.site.register(Produit)
admin.site.register(Commande)
admin.site.register(Panier)