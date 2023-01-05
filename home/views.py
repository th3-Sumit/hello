from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'variable':"this is variable",
        'name':"Sumit kumar"
    }
    
    return render(request, 'index.html', context)
    # return HttpResponse("This is homepage")

def reviews(request):
    return render(request, 'reviews.html')
    # return HttpResponse("This is About Page")

def Contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        city = request.POST['city']
        state = request.POST['state']
        # pincode = request.POST['pincode']

        contactinfo = User.objects.create_user(name, email, address)
        contactinfo.phone = phone
        contactinfo.city = city
        contactinfo.state = state
        # contactinfo.pincode = pincode
        contactinfo.date = datetime.today()
        contactinfo.save()

        messages.success(request, "your request has been send to the admin plz wait for while")
        
        return redirect('home')

    return render(request, 'contact.html')
    # return HttpResponse("This is a contact page")
    

def logIn(request):
    
    # if request.method == "POST":
    #     username = request.POST['username']
    #     fname = request.POST['fname']
    #     lname = request.POST['lname']
    #     email = request.POST['email']
    #     pass1 = request.POST['pass1']
    #     pass2 = request.POST['pass2']

    #     myuser = User.objects.create_user(username, email, pass1)
    #     myuser.first_name = fname
    #     myuser.last_name = lname

    #     myuser.save()

    #     messages.success(request, "your Account has been successfully created.")

    #     return redirect('home')

    return render(request, 'login.html')
    # return HttpResponse("this is login and signup page.")

def sign_in(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "your Account has been successfully created.")

        return redirect('home')


    return render (request, 'sign-in.html')

def myteam(request):
    return render(request, 'myteam.html')
    # return HttpResponse("this is my team")


def product(request):
    return render(request, 'product.html')

def login_page2 (request):
    return render (request, 'loginpage02.html')

def logInsignup(request):
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        log = User.objects.create_user(username, password)
        log.save()

        messages.success(request, "Now your account has loged in. Enjoy...!!")


    return render(request, 'logIn&signup.html')

