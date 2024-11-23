from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from boutique.models import Produit, Panier, Commande
from django.urls import reverse
from django.shortcuts import redirect

def index(requete):
    produits = Produit.objects.all()
    return render(requete, 'boutique/index.html' , context= {"produits": produits})
def detail_produit(requete, slug):
    produit = get_object_or_404(Produit, slug=slug)
    return render(requete, 'boutique/detail.html', context = {"produit": produit})

def ajouter_au_panier(requete, slug):
    if not requete.user.is_authenticated:
        return redirect('connexion')
    user = requete.user 
    produit = get_object_or_404(Produit, slug=slug)
    panier, _ = Panier.objects.get_or_create(user=user)
    commande = Commande.objects.filter(user=user, commandé=False, produit=produit).first()
    if commande:
        commande.quantite += 1
        commande.save()
    else:
        commande = Commande.objects.create(user=user, produit=produit, quantite=1, commandé=False)
        panier.commandes.add(commande)
    panier.save()

    return redirect(reverse("produit" , kwargs={"slug" : slug}))  

def panier(requete):
    panier = get_object_or_404(Panier, user=requete.user)
    commandes = panier.commandes.all()
    total = panier.total()
    total_commande = [
        {"commande": commande, "total": commande.quantite * commande.produit.prix}
        for commande in commandes
    ]
    total_panier = sum(item["total"] for item in total_commande)
    
    return render(
        requete,
        'boutique/panier.html',
        context={
            "commandes": total_commande,
            "total_panier": total_panier,
        },
    )
    return render(requete,'boutique/panier.html', context={"commandes" : panier.commandes.all()})

def supp_panier(requete):
    panier = Panier.objects.filter(user=requete.user).first()
    if panier:
        panier.commandes.all().delete()
        panier.delete()

    return redirect('index')    
