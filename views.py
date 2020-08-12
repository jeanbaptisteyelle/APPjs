from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as log,logout
from django.core.validators import validate_email
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    datas = {

    }
    return render(request, 'pages/index.html', datas)


def appointment(request):
    datas = {

    }
    return render(request, 'pages/appointment.html', datas)

def blog_single(request):
    datas = {

    }
    return render(request, 'pages/blog-single.html', datas)

def login(request):
    datas = {

    }
    return render(request, 'pages/login.html', datas)


def register(request):
    datas = {

    }
    return render(request, 'pages/register.html', datas)

def senddata(request):
    
    postdata = json.loads(request.body.decode('utf-8'))
    
    username = postdata['username']
    email = postdata['email']
    password = postdata['password']
    confirm = postdata['confirm']
    issuccess = false
    if username != '':
        issuccess = true
    else:
        issuccess = false
        
    datas = {
        'success':issuccess,
        'username':username
    }
    return JsonResponse(datas, safe=False)

@csrf_exempt
def postdata(request):
    message = " "
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirm = request.POST.get('confirm')
    issucces = False
    if password != confirm or not password or password.isspace():
            success = True
            message = "mot de passe incorrect"
            print("mot de passe incorrect")
    else:
        message = "correct"
        print("success")
        try:
            validate_email(email)
            isemail = True
            if username and not username.isspace():
                try:
                    issucces = False
                    try:
                        exist_user = User.objects.get(username=username)
                    except :
                        exist_user = User.objects.get(email=email)
                    message = "un utilisateur avec le même username ou email est déjà connecté"
                except:
                    issucces = True
                    user = User(
                        username=username,
                        email=email,
                        password=password,
                    )
                    user.save() 
                    user.password = password
                    user.set_password(user.password)
                    user.save()
                    
                    print(username,email,password,confirm)
            else:
                message = "informations incorect, veuillez vérifier vos informations" 
                issucces = False

        except Exception as e:
                success = True 
                print("5", e)
                message = "l'inscription a échoué, veuillez remplir le formulaire correctement!"
                print("inscription echoué")
    datas = {
        'success': issucces,
        'username': username,
        'message': message,
    }
    return JsonResponse(datas, safe=False)

@csrf_exempt
def is_login(request):
    password = request.POST.get('password')
    username = request.POST.get('username')
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        log(request, user)
        message = "Bienvenue" + user.username
        isSuccess = True
    else:
        print("login echoué ")
        message = "veuillez vérifier les informations entrées"
        isSuccess = False
        
    datas = {
        'message': message,
        'success': isSuccess,
    }
    return JsonResponse(datas, safe=False)