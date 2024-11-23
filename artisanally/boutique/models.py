from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse
from artisanally.settings import AUTH_USER_MODEL


class Produit(models.Model):
    nom = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    prix = models.FloatField(default=0.0)
    quantite = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="produits", blank=True, null=True)

    def __str__(self):
        return self.nom
    
    def get_absolute_url(self):
        return reverse("produit", kwargs={"slug": self.slug})

   
class Commande(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete = models.CASCADE) 
    produit = models.ForeignKey(Produit, on_delete = models.CASCADE)
    quantite = models.IntegerField(default=1)
    commandé = models.BooleanField(default=False)
    date_commande = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.produit.nom} ({self.quantite} articles)"
    

class Panier(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    commandes = models.ManyToManyField('Commande', related_name='panier')
    

    def __str__(self):
        return self.user.username
    
    def delete(self, *args, **kwargs):
        for commande in self.commandes.all():
            commande.commandé = True
            commande.date_commande = timezone.now()
            commande.save()
        
        self.commandes.clear()
        super().delete(*args, **kwargs) 
    def total(self):
        return sum(commande.produit.prix * commande.quantite for commande in self.commandes.all())       


    



# Create your models here.
