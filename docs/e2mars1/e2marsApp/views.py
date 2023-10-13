import json
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import os
from django.conf import settings
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from io import BytesIO
import base64
from django import template
import json
import os
from django.shortcuts import render
from django.http import HttpResponse
import subprocess
from google.cloud import dialogflow
from google.protobuf.json_format import MessageToJson
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from django.core.files.storage import FileSystemStorage

# Create your views here.


def Home(required):
    if required.method == "POST":
        email = required.POST.get('email')
        name = required.POST.get('name')
        service = required.POST.get('service')
        service_Date = required.POST.get('service_date')
        requests = required.POST.get('requests')
        print(f'Email: {email} Password: {name} Sevice: {service} Sevice_Date: {service_Date} Request: {requests}')
    if required.method == "POST":
        subemail = required.POST.get('subemail')
        print(f"Subscribe Email : {subemail}")
    return render(required, "index.html")


def Transportation(required):
    return render(required, "FindItems.html")


def Renting(required):
    if required.method == "POST":
        search = required.POST.get('search')
        email = required.POST.get('email')
        print(f"search: {search} email: {email}")
    return render(required, "Selling.html")


def Selling(required):
    if required.method == "POST":
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
    if required.session['error'] == 4:
        required.session['error'] = 1
        print( required.session['error'] )
        return render(required, "logins.html", {'error': 'Account Not Found'})
    if required.method == "POST":
        email = required.POST.get('email')
        password = required.POST.get('password')
        import DatabaseConnection
        DatabaseConnection.connection.reconnect()
        DatabaseConnection.TABLE_creation_ForTaxi_Driver_in_User_Detail()
        print(required.session['error'])
        required.session['error'] = 'one1'
        if required.session['error'] == 'one':
            print('The session is None')
            return render(required, "logins.html", {'error': 'I'})
        if email:
            required.session['email'] = email
            required.session['password'] = password

            return HttpResponseRedirect('DashBoard')

    return render(required, "logins.html")


def Product(required):
    account_type = required.session['Account_Type']
    print(account_type)

    if account_type == "car-service":
        print("Validation Completed As Successfully")
        return render(required, "ProductUpload.html", {'Pname': 'Car Name', 'Pprice': 'Plate', 'Pdescription': 'Car document', 'Pnumber': 'Service', 'password': 'Car Description' })

    if required.method == "POST":
        pname = required.POST.get('Pname')
        pprice = required.POST.get('Pprice')
        pdescription = required.POST.get('Pdescription')
        pnumber = required.POST.get('Pnumber')
        ppassword = required.POST.get('password')

        gender = required.POST.get('gender')
        print(
            f'{pname} || {pprice} || {pdescription} || {pnumber} || {ppassword} || {pconpassword} || {gender}')

        id = required.session['Account_ID']

    return render(required, "ProductUpload.html", {})


def Register(required):
    if required.method == "POST":
        if 'imageUpload' in required.FILES:
            uploaded_file = required.FILES['imageUpload']
            print(uploaded_file.name)
            fs = FileSystemStorage()
            image = fs.save(uploaded_file.name, uploaded_file)
            print(image)

        else:
             url = f"media/download.png"
             print("Not Found")

        email = required.POST.get('email')
        name = required.POST.get('name')
        service = required.POST.get('service')
        phone = required.POST.get('phone')
        password = required.POST.get('password')
        conpassword = required.POST.get('conpassword')
        import DatabaseConnection
        DatabaseConnection.connection.reconnect()
        DatabaseConnection.saving_in_MySQL_User_details_with_images(f"media/{image}", name, email, phone, service, password)
        print(f'Photo: {image} Email: {email} || Name: {name} || Sevice: {service} || Phone Number: {phone} || Password: {password} || Confirm Password: {conpassword}')

    return render(required, "Register.html")

register = template.Library()

@register.filter
def b64encode(value):
    return base64.b64encode(value).decode('utf-8')
# setting AppConfig
from django.apps import AppConfig
class YourAppNameConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'e2mars1App'
    def ready(self):
        import e2mars1App.custom_filters

def DashBoard(required):
    required.session['error'] = 'one'
    if required.method == "POST":
        dashsearch = required.POST.get('dashsearch')
        print(f"Subscribe From Team Email : {dashsearch}")
    import DatabaseConnection
    DatabaseConnection.connection.reconnect()
    email = required.session['email']
    password = required.session['password']

    required.session['error'] = None
    alldata = [{'name': "Baraka", 'age': 23}, {'name': "Daniel", 'age': 32}, {'name': "Luc", 'age': 12}]
    data = DatabaseConnection.Read_in_MySQL_Image(email, password)
    if data == 'one':
       required.session['error'] = 4
       print(required.session['error'])
       return HttpResponseRedirect('LogIn',{'error','Account Not Found'})
    else:
        required.session['error'] = 'one'
    required.session['error'] = 1
    required.session['Account_Type'] = data[5]
    required.session['Account_ID'] = data[0]
    print(data[5])
    required.session['error'] = 'one'
    return render(required, 'DashBoard.html', {'alldata': alldata, 'image': b64encode(data[1]), 'name': data[2]})

def convert(data):
    if isinstance(data, bytes):
        return data.decode('ascii')
    if isinstance(data, dict):
        return dict(map(convert, data.items()))
    if isinstance(data, tuple):
        return map(convert, data)

    return data


def detect_intent_text(project_id, session_id, text, language_code='en-US'):
    project_root = os.path.dirname(os.path.abspath(__file__))
    credentials_file_path = os.path.join(project_root, "AidriveCredentials.json")
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_file_path

    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )

    return response.query_result


@csrf_exempt
@require_http_methods(['POST'])
def chatbot_view(request):
    print('body', request.body)
    imput_dict = convert(request.body)
    if request.method == 'POST':
        # user_input = request.POST.get('message', '')
        user_input = json.loads(imput_dict)['message']
        print(f"User Input: {user_input}")
        if user_input.lower() == 'exit':
            return JsonResponse({'botResponse': 'Goodbye!'})
        response = detect_intent_text('aidrive-project', '0123D34', user_input)
        return JsonResponse({'botResponse': response.fulfillment_text})
        # return HttpResponse(response.fulfillment_text, status=200)

    else:
        return JsonResponse({'error': 'Invalid request method'})
def Taxi(required):
    if required.method == "POST":
        dashsearch = required.POST.get('dashsearch')
        print(f"Subscribe From Team Email : {dashsearch}")
    return render(required, "Taxi.html")


def convert(data):
    if isinstance(data, bytes):
        return data.decode('ascii')
    if isinstance(data, dict):
        return dict(map(convert, data.items()))
    if isinstance(data, tuple):
        return map(convert, data)

    return data


def detect_intent_text(project_id, session_id, text, language_code='en-US'):
    project_root = os.path.dirname(os.path.abspath(__file__))
    credentials_file_path = os.path.join(project_root, "AidriveCredentials.json")
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_file_path

    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )

    return response.query_result

@csrf_exempt
@require_http_methods(['POST'])
def chatbot_view(request):
    print('body', request.body)
    imput_dict = convert(request.body)
    if request.method == 'POST':
        # user_input = request.POST.get('message', '')
        user_input = json.loads(imput_dict)['message']
        print(f"User Input: {user_input}")
        if user_input.lower() == 'exit':
            return JsonResponse({'botResponse': 'Goodbye!'})
        response = detect_intent_text('aidrive-project', '0123D34', user_input)
        return JsonResponse({'botResponse': response.fulfillment_text})
        # return HttpResponse(response.fulfillment_text, status=200)

    else:
        return JsonResponse({'error': 'Invalid request method'})
