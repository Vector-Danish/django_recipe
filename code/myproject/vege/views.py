from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def receipes(request): 
    if request.method == "POST":
        data = request.POST

        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        Recipe.objects.create(
            receipe_image = receipe_image,
            receipe_description = receipe_description,
            receipe_name = receipe_name,
            )
        
        return redirect('/receipes/')
    
    queryset = Recipe.objects.all()

    if request.GET.get('search_food'):
        # print(request.GET.get('search_food'))
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search_food'))

    context = {'recipes': queryset }
    return render(request, "recipies.html", context=context) 

def delete_recipe(request, id):

    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/receipes/')


def edit_recipe(request, id):
    queryset = Recipe.objects.get(id = id)

    if request.method == "POST":
        data = request.POST 

        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description

        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect('/receipes/')

    context = {'recipe': queryset }

    
    return render(request, "editrecipe.html", context=context)  

def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid username')
            return redirect('/login/')
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, 'Invalid password')
            return redirect('/login/')
        
        else:
            login(request, user)
            return redirect('/receipes/')

    return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, "Username already taken")
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,

        )

        user.set_password(password)
        user.save()

        messages.info(request, "Account created successfuly")
        return redirect('/register/')


    return render(request,'register.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')