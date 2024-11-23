
from django.contrib import admin
from django.urls import path
from boutique.views import index, detail_produit, ajouter_au_panier, panier, supp_panier
from django.conf import settings
from django.conf.urls.static import static
from compte.views import signe, logout_user, login_user

urlpatterns = [
    path('' , index, name='index'),
    path('admin/', admin.site.urls),
    path('signe/', signe, name = "signe" ),
    path('connexion/', login_user, name = "connexion" ),
    path('logout/', logout_user, name = "logout" ),
    path('panier', panier, name="panier"),
    path('panier/supprimer/', supp_panier, name="supprimer-panier"),
    path('produit/<str:slug>/', detail_produit, name = "produit"),
    path('produit/<str:slug>/ajouter_au_panier', ajouter_au_panier, name = "ajouter_au_panier"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


