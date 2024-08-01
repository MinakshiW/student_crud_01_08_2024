from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def signview(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/a2/lv/')
    return render(request, 'auth_app/signup.html', {'form': form})

def loginview(request):
    if request.method == 'POST':
        u = request.POST.get('unm')
        p = request.POST.get('pwd')
        user = authenticate(username=u, password=p)
        if user!=None:
            login(request, user)
            return redirect('/a1/sv/')
    return render(request, 'auth_app/login.html', {})

def logoutview(request):
    logout(request)
    return redirect('/a2/lv/')


