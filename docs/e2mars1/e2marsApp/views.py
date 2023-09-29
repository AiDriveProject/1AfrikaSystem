from django.shortcuts import render

# Create your views here.
def Home(required):
    return render(required, "index.html")

def Transportation(required):
    return render(required, "FindItems.html")

def Renting(required):
    return render(required, "Selling.html")

def Selling(required):
    return render(required, "Selling.html")

def OrderFood(required):
    return render(required, "Restaurant.html")
def Repair(required):
    return render(required, "Repair.html")

def Team(required):
    return render(required, "team.html")

def LogIn(required):
    return render(required, "logins.html")

def Product(required):
    return render(required, "ProductUpload.html")

def Register(required):
    return render(required, "Register.html")

def DashBoard(required):
    return render(required, "DashBoard.html")