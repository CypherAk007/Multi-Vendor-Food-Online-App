from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.
from .forms import UserForm
from .models import User
from django.contrib import messages,auth
from vendor.forms import VendorForm
from accounts.models import UserProfile

def registerUser(request):
    if request.method == "POST":
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            # Method -1 
            # # what ever data we have in form will be assigned to user  
            # password = form.cleaned_data['password']
            # user = form.save(commit=False)
            # user.set_password(password)
            # user.role = User.CUSTOMER
            # # save the modified user 
            # user.save()

            # Method -2 
            # create the user using create_user Method 
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email = email,password=password)
            user.role = User.CUSTOMER
            user.save()
            messages.success(request,"Your account has been registered Successfully!!")
            print('user created')
            return redirect('registerUser')
        else:
            print('invalid form')
            print(form.errors)
    else:
        form = UserForm()

    context = {
        'form':form,
    }
    return render(request,'accounts/registerUser.html',context)

def registerVendor(request):
    # Combine user form and vendor form(vname&vlicense fields)
    if request.method == 'POST':
        # store the data and create the user
         
        # reiceve the form 
        form = UserForm(request.POST)
        # Recieve the files if form has any files
        v_form = VendorForm(request.POST,request.FILES)
        if form.is_valid() and v_form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email = email,password=password)
            user.role = User.VENDOR
            user.save()
            
            vendor = v_form.save(commit=False) #so that we can assign value for user,user_profile in vendor model
            vendor.user = user
            # get user profile from user 
            user_profile = UserProfile.objects.get(user = user)
            vendor.user_profile = user_profile
            vendor.save()
            messages.success(request,'Your account has been registerd successfully! Please wait for Approval')
            return redirect('registerVendor')

        else:
            print('invalid Forms')
            print(form.errors)
        pass 
    else:
        form = UserForm()
        v_form = VendorForm()
    context ={
        'form':form,
        'v_form':v_form,
    }
    return render(request,'accounts/registerVendor.html',context)

def login(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']
        # Check if email and password belongs to user or not
        # Django inbuilt Authincate 
        user = auth.authenticate(email=email,password=password) #returns user to whome the user belongs to
        if user is not None:
            # This auth package logs the user in 
            auth.login(request,user)
            messages.success(request,'You are now Logged in.')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid login credentials')
            return redirect('login')
    return render(request,'accounts/login.html')


def logout(request):
    return render(request)


def dashboard(request):
    return render(request,'accounts/dashboard.html')