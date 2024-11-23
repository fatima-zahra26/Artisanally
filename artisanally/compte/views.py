from django.contrib.auth import get_user_model, login, logout,authenticate
from django.shortcuts import render, redirect

User = get_user_model()
def signe (requete):
    if requete.method == "POST":
        username = requete.POST.get("username")
        password = requete.POST.get("password")
        user = User.objects.create_user(username=username,
                                        password=password)
        login(requete, user)
        return redirect('index')
    return render(requete, 'compte/signe.html')
def login_user(requete):
    if requete.method == "POST":
        username = requete.POST.get("username")
        password = requete.POST.get("password")
        user = authenticate(username = username, password=password)
        if user:
            login(requete, user)
            return redirect('index')
    return render(requete, 'compte/connexion.html')    
def logout_user(requete):
    logout(requete)
    return redirect('index')
