from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout # type: ignore
# Create your views here.

def logins(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request.POST, username= username, password=password)
        if user is not None:
            login(request, user) # type: ignore
            return redirect("index")
        else:
            return render(request, "authentication/logins.html")
    return render(request, "authentication/logins.html")

def logouts(request):
    logout(request)
    return render(request, 'authentication/logout.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('logins')
    else:
        form = UserCreationForm()
    return render(request, "authentication/signup.html", {"form": form})
        








