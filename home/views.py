from django.shortcuts import render, redirect
from .models import Contact, Image
from datetime import datetime
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
 
def index(request):
    users = User.objects.all()
    images = Image.objects.all()
    return render(request, "index.html", {"users": users, "images": images}) 


def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"] 
        Contact(name=name, email=email, subject=subject, message=message, date=datetime.today()).save()
        print("contact data send successfull........")
        messages.info(request, "message success")

    return render(request, "contact.html")


def login(request):
    # login user 
    
    if request.method == "POST":     
        username = request.POST["username"]
        password = request.POST["password"]   
        contact = auth.authenticate(username=username, password=password )

        if contact is not None:
            auth.login(request, contact)
            print("user avilable login success")
            messages.info(request, "success welcom {}".format(username))
            return redirect('/')
        else:
            print("user not avilable ")
            messages.info(request, "not avilable") 
            
    else: 
        return render(request, "login.html")



    return render(request, "login.html")



def signin(request):
    if request.method == "POST":
        user_name = request.POST["user_name"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"] 
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == confirm_password:
            if User.objects.filter(username=user_name).exists():
                print("user name already exist ........")
                messages.error(request, "user name already exist ")  

            else:
                User.objects.create_user(username=user_name, email=email, first_name=first_name, last_name=last_name, password=password).save()
                print("sign in data send successfull........")
                messages.success(request, "SignIn success")  
                return redirect('/login')
            
        else:
            print("password not matching........")
            messages.error(request, "password not matching")

    return render(request, "signin.html")


def logout(request): 
        auth.logout(request)
        return redirect('/login')


        
def image(request): 
    if request.method == "POST":
        pic = request.POST["image"]
        Image(image = pic).save()
        print("successfull........")
        messages.success(request, "image send success")
    return render(request, "contact.html") 