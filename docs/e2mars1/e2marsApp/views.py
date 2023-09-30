from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(required):
    if required.method=="POST":
        email = required.POST.get('email')
        name = required.POST.get('name')
        service = required.POST.get('service')
        service_Date = required.POST.get('service_date')
        requests = required.POST.get('requests')
        print(f'Email: {email} Password: {name} Sevice: {service} Sevice_Date: {service_Date} Request: {requests}')
    if required.method == "POST":
        subemail=required.POST.get('subemail')
        print(f"Subscribe Email : {subemail}")
    return render(required, "index.html")

def Transportation(required):
    return render(required, "FindItems.html")

def Renting(required):
    if required.method=="POST":
        search = required.POST.get('search')
        email = required.POST.get('email')
        print(f"search: {search} email: {email}")
    return render(required, "Selling.html")

def Selling(required):
    if required.method=="POST":
        search = required.POST.get('search')
        email = required.POST.get('email')
        print(f"search: {search} email: {email}")
    return render(required, "Selling.html")

def OrderFood(required):
    if required.method == "POST":
        oneperson = required.POST.get('oneperson')
        name = required.POST.get('name')
        message = required.POST.get('message')
        phone = required.POST.get('phone')
        date = required.POST.get('date')
        hours = required.POST.get('hours')
        print(
            f'Person: {oneperson} || Name: {name} || Message: {message} || Phone Number: {phone} || Date: {date} || Hours: {hours}')

    return render(required, "Restaurant.html")
def Repair(required):
    return render(required, "Repair.html")

def Team(required):
    if required.method == "POST":
        TeamEmail = required.POST.get('TeamEmail')
        print(f"Subscribe From Team Email : {TeamEmail}")
    return render(required, "team.html")

def LogIn(required):
    if required.method=="POST":
        email = required.POST.get('email')
        password = required.POST.get('password')
        print(f'Email: {email} Password:{password} ')
    return render(required, "logins.html")


def Product(required):
    if required.method == "POST":
        pname = required.POST.get('Pname')
        pprice = required.POST.get('Pprice')
        pdescription = required.POST.get('Pdescription')
        pnumber = required.POST.get('Pnumber')
        ppassword = required.POST.get('password')
        pconpassword = required.POST.get('conpassword')
        gender = required.POST.get('gender')
        print(
            f'{pname} || {pprice} || {pdescription} || {pnumber} || {ppassword} || {pconpassword} || {gender}')

    return render(required, "ProductUpload.html")

def Register(required):
    if required.method=="POST":
        email = required.POST.get('email')
        name = required.POST.get('name')
        service = required.POST.get('service')
        phone = required.POST.get('phone')
        password = required.POST.get('password')
        conpassword = required.POST.get('conpassword')
        print(f'Email: {email} || Name: {name} || Sevice: {service} || Phone Number: {phone} || Password: {password} || Confirm Password: {conpassword}')
    return render(required, "Register.html")

def DashBoard(required):
    if required.method == "POST":
        dashsearch = required.POST.get('dashsearch')
        print(f"Subscribe From Team Email : {dashsearch}")
    return render(required, "DashBoard.html")

