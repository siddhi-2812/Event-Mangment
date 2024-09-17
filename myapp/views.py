from django.contrib import messages
from django.shortcuts import redirect, render

from myapp.models import *


# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def event(request):
    return render(request,"events.html")

def Contact(request):
    return render(request,"contact.html")

def gallary(request):
    return render(request,"gallery.html")

def login(request):
    return render(request,"Login.html")

def register(request):
    return render(request,"Signup.html")

def forgot(request):
    return render(request,"forgot.html")
def reset(request):
    return render(request,"reset.html")


def wedding(request):
    return render(request,"wedding.html")
def marraige(request):
    return render(request,"marraige.html")
def haldi(request):
    return render(request,"haldi.html")
def mehndi(request):
    return render(request,"mehndi.html")
def reception(request):
    return render(request,"reception.html")
def sangeet(request):
    return render(request,"sangeet.html")

def birthday(request):
    return render(request,"birthday.html")
def theme(request):
    return render(request,"theme.html")

def Booking(request):
    return render(request,"booking.html")

def college(request):
    return render(request,"college.html")
def graduation(request):
    return render(request,"graduation.html")
def festival(request):
    return render(request,"festival.html")
def fresher(request):
    return render(request,"fresher.html")
def annual(request):
    return render(request,"annual.html")

def insert_data(request):
    if request.method == "POST":
       name=request.POST.get("Name")
       email=request.POST.get("Email")
       password=request.POST.get("upasssword")
       phone=request.POST.get("uphone")
       queary= User.objects.filter(email=email)
       if queary.exists():
          messages.error(request,'Email Already Exists!!')
          return render(request,"Signup.html")
       else:
           queary=User(Name=name,contactno=phone,email=email,password=password)
           queary.save()
           messages.success(request,'REGISTRATION SUCUESSFUL!!')
           return render(request,"Login.html")
    else:
        messages.error(request,'SORRY!! UNABLE TO REEQUEST')
        return render(request,"Signup.html")

def CheckLogin(request):
     useremail=request.POST['Email']
     userpwd=request.POST['Password']
     try:
         query=User.objects.get(email=useremail,password=userpwd)
         request.session['useremail']=query.email
         request.session['user_id'] = query.id
         request.session.save()
         print(request.session['user_id'])
     except User.DoesNotExist:
         query=None
     if query is None:
         messages.info(request, 'Account Does Not Exists !! Please Sign Up')
         return render(request, "Signup.html")
     else:
         messages.success(request,'LOGIN SUCCESSFUL!!')
     return render(request,"index.html")

def logout(request):
    try:
        del request.session['useremail']
        del request.session['user_id']
    except:
        pass
    return redirect(index)
def booking_insert(request):
    try:
      if request.method == "POST":
       lid= request.session['user_id']
       FirstName=request.POST.get("FirstName")
       LastName= request.POST.get("LastName")
       Email=request.POST.get("Email")
       Phone=request.POST.get("Phone")
       Category = request.POST.get("Category")
       time = request.POST.get("time")
       Sub_Category = request.POST.get("Sub_Category")
       Location = request.POST.get("Location")
       Date = request.POST.get("Date")
       Package = request.POST.get("Package")
       Details = request.POST.get("Details")
       queary=BOOKING(User_Id=User(id=lid),Time=time,Category=Category,subcat=Sub_Category,Package=Package,First_Name=FirstName,Last_Name=LastName,Phone_no=Phone,Email=Email,date=Date,Location=Location,details=Details)
       queary.save()
       messages.success(request,'BOOKING IS NOT SUCCESSFUL !! PLEASE DO A PAYMENT')
       return render(request, "Payment.html")
    except:
        return redirect("/login")

def contact_data(request):
       name=request.POST.get("Name")
       email=request.POST.get("Email")
       subject=request.POST.get("Subject")
       message=request.POST.get("Message")
       queary=contact(Name=name,Email=email,Subject=subject,Message=message)
       queary.save()
       messages.success(request,'DETAILS ARE SUCUESSFULLY ADDED WE WILL CONTACT YOU SOON!!')
       return render(request,"contact.html")

def forgotpassword(request):
    if request.method == 'POST':
        username = request.POST['Email']
        try:
            user = User.objects.get(email=username)

        except User.DoesNotExist:
            user = None
        #if user exist then only below condition will run otherwise it will give error as described in else condition.
        if user is not None:
            #################### Password Generation ##########################
            import random
            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                       'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

            nr_letters = 6
            nr_symbols = 1
            nr_numbers = 3
            password_list = []

            for char in range(1, nr_letters + 1):
                password_list.append(random.choice(letters))

            for char in range(1, nr_symbols + 1):
                password_list += random.choice(symbols)

            for char in range(1, nr_numbers + 1):
                password_list += random.choice(numbers)

            print(password_list)
            random.shuffle(password_list)
            print(password_list)

            password = ""  #we will get final password in this var.
            for char in password_list:
                password += char

            ##############################################################


            msg = "hello here it is your new password  "  +password   #this variable will be passed as message in mail

            ############ code for sending mail ########################

            from django.core.mail import send_mail

            send_mail(
                'Your New Password',
                msg,
                'travelyourway.way@gmail.com',
                ['jaivinmakwana@gmail.com','nandwanadaksh17@gmail.com','renish15503@gmail.com'],
                fail_silently=False,
            )
            # NOTE: must include below details in settings.py
            # detail tutorial - https://www.geeksforgeeks.org/setup-sending-email-in-django-project/
            # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
            # EMAIL_HOST = 'smtp.gmail.com'
            # EMAIL_USE_TLS = True
            # EMAIL_PORT = 587
            # EMAIL_HOST_USER = 'mail from which email will be sent'
            # EMAIL_HOST_PASSWORD = 'pjobvjckluqrtpkl'   #turn on 2 step verification and then generate app password which will be 16 digit code and past it here

            #############################################

            #now update the password in model
            cuser = User.objects.get(email=username)
            cuser.password = password
            cuser.save(update_fields=['password'])

            print('Mail sent')
            messages.info(request, 'mail is sent')
            return redirect(index)

        else:
            messages.info(request, 'This account does not exist')
    return redirect(index)

def editprofile(request):
    Login_Id = request.session['user_id']
    query=User.objects.get(id=Login_Id)
    return render(request,"editprofile.html",{"userdata":query})

def updateprofile(request):
    Name=request.POST.get("Name")
    Email=request.POST.get("Email")
    Phone=request.POST.get("uphone")
    Password = request.POST.get("upassword")
    Login_Id = request.session['user_id']
    query= User.objects.get(id=Login_Id)
    query.Name = Name
    query.email = Email
    query.contactno = Phone
    query.password = Password
    query.save()
    messages.success(request,"Edit Profile Sucuessfully")
    return redirect(index)

def Payment(request,bid):
    data =BOOKING.objects.get(id=bid)
    return render(request,"Payment.html",{'bookingdata':data})


def payment_insert(request):
    if request.method == "POST":
        Login_Id = request.session['user_id']
        name = request.POST.get("Name")
        Card_No = request.POST.get("Number")
        cvv = request.POST.get("cvv")
        expiry_date = request.POST.get("date")
        query = Card(User_Id=User(id=Login_Id),Name=name,card_num=Card_No,Cvv=cvv,Expiry_Date=expiry_date)
        query.save()
        messages.success(request,'BOOKING SUCCESSFUL!!')
        return render(request, "index.html")
    else:
        messages.error(request,'SORRY!! UNABLE TO DO Payment')
        return render(request,"Payment.html")
