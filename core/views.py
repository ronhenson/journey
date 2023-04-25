from django.shortcuts import render, redirect

from .forms import SignupForm

def index(request):
    hello = "Welcome to index page"

    return render(request, 'core/index.html', {
        'hello': hello,
    })

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            
        return redirect("/login")
    else:
        form = SignupForm()
        
    return render(request, 'core/signup.html', {
        'form': form
    })
