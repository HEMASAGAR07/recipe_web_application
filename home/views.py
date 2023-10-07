from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "home.html")

@login_required(login_url="/login/")
def recipe_view(request):
    if request.method == "POST":
        data = request.POST
        recipe_name = request.POST.get('recipe_name')
        recipe_discription = request.POST.get('recipe_discription')
        recpie_image = request.FILES.get('recpie_image')

        print(recipe_name)
        print(recipe_discription)

        recipe.objects.create(

            recipe_name=recipe_name,
            recipe_discription=recipe_discription,
            recpie_image=recpie_image,)

        return redirect('/recipe')
    recipes = recipe.objects.all()

    if request.GET.get('search'):
        recipes =  recipes.filter(recipe_name__icontains = request.GET.get('search'))
        recipes = recipes.filter(recipe_discription__icontains=request.GET.get('search'))

    return render(request, "recipe.html", {'recipes': recipes})

@login_required(login_url="/login/")
def update_recipe(request, id):
    recipes = recipe.objects.get(id=id)
    context = {'recipes': recipes}

    if request.method == "POST":
        data = request.POST
        recipe_name = request.POST.get('recipe_name')
        recipe_discription = request.POST.get('recipe_discription')
        recpie_image = request.FILES.get('recpie_image')

        recipes.recipe_name=recipe_name
        recipes.recipe_discription=recipe_discription

        if recpie_image:
            recipes.recpie_image=recpie_image

        recipes.save()
        return redirect('/recipe')
    return render(request, "update_recipe.html", context)

@login_required(login_url="/login/")
def delete_recipe(request, id):
    recipes=recipe.objects.get(id=id)
    recipes.delete()




    return redirect('/recipe/')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/recipe/')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('/login/')

    return render(request, 'loginpage.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

def register_page(request):

    if request.method == "POST":
        first_name=request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, "User already exists.")
            return redirect('/register/')

        user = User.objects.create(
        first_name=first_name,
        last_name=last_name,
        username= username,

        )
        user.set_password(password)
        user.save()
        messages.info(request, "Account created succesfully")
        return redirect('/register/')



    return render(request, 'register.html')

