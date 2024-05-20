from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import UserModel , ServiceMan, Services, Orders
# Create your views here.
def index(request):

    return render(request, 'index.html')

def about(request):

    return render(request, 'about.html')

def adminLogin(request):

    return render(request, 'admin_login.html')


def signin(request):
    if request.method =="POST":
        uname = request.POST["username"] 
        pass1 = request.POST["password"]

        user= authenticate(username=uname,password=pass1)
        if user is not None:
            login(request,user)
            if(user.get_username()=="admin"):
                messages.success(request,"You'er LoggedIn")
                return redirect("admin1")
                
            else:
                messages.success(request,"You'er LoggedIn")
                return redirect("user")
                
        else:
            messages.success(request,"User Invalid")    
            return redirect("login")

    return render(request, 'login.html')



def signup(request):
    
    if request.method =="POST":

        uname = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email  = request.POST["email"]
        
        number = request.POST["number"] 
        pass1 = request.POST["password"]
        pass2 = request.POST["rePass"]


        if UserModel.objects.filter(username=uname):
            messages.error(request,"this user is already exist")
            return redirect("signup")

        elif UserModel.objects.filter(email =email):
            messages.error(request,"this email is already associated")  
            return redirect("signup")   
        
        elif (pass1 != pass2):
            messages.error(request,"password didn't match")  
            return redirect("signup")   

        else:
            
            user = UserModel.objects.create_user(username = uname,email =email, password= pass1)
            user.first_name= fname
            user.last_name= lname
            user.mobile_number =number
            try:
                img = request.FILES["img"]
                user.profile_img =img
            except:
                pass    
            user.save()
            messages.error(request,"your account is Created")   
            return redirect("home") 
           


    return render(request,"register.html")

def myprofile(request):
    return render(request, "profile.html")



def allUsers(request):
    data = UserModel.objects.all()
    return render(request,"user.html",{"dt": data})


def admin1(request):
    
    return render(request,"admin.html")


def allServiceMan(request):
    serviceall = ServiceMan.objects.all()
    return render(request, "service-men.html",{"serviceDt":serviceall})



def user(request):

    services = Services.objects.all()
   
    
    
    return render(request, "user_panel.html",{"services":services})


def bookNow(request,id):
    user = request.user
    
    # service = Services.objects.get(id=id)
    
    service = Services.objects.get(id=id)
    
    # Create a new Orders instance with the retrieved service and user
    Orders.objects.create( serviceId=service,user=user)
    
    messages.success(request, "order booked")
    
    return redirect("user")


def order(request):
    allorders = Orders.objects.all()


    return render(request, "order.html",{"alloders":allorders})


def myorder(request):
    user= request.user
    myorders = Orders.objects.filter(user=user)


    return render(request, "myorder.html",{"myorders":myorders})


def services(request):

    services = Services.objects.all()

    return render(request, "services.html",{"services":services})


def addServices(request):
    
    if request.method =="POST":
        service_name= request.POST["ser_name"]
        service_img= request.FILES["ser_img"]
        service_diss= request.POST["ser_diss"]

        data= Services.objects.create(service_name=service_name,
                                      service_img=service_img,
                                      service_diss=service_diss)
        data.save()
        messages.success(request,"Service Added")

    return render(request, "add-service.html")

def delServices(request):
    services = Services.objects.all()
    return render(request, "delete-service.html",{"services":services})


def deleteServices(request,id):

    data1 = Services.objects.get(id=id)
    data1.delete()
    messages.success(request,"Deleted")
    return redirect("delServices")


def deleteUser(request,id):
        data1 = UserModel.objects.get(id=id)
        data1.delete()
        messages.success(request,"Deleted")
        return redirect("allUser")


def deleteOrder(request,id):

        data1 = Orders.objects.get(id=id)
        data1.delete()
        messages.success(request,"Deleted")
        return redirect("order")


def deleteServiceman(request,id):
    data1 = ServiceMan.objects.get(id=id)
    data1.delete()
    messages.success(request,"Deleted")
    return redirect("allServiceMan")


def signout(request):
    logout(request)
    return redirect("home")


