from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.
from .forms import UserForm
from .models import User

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
            print('user created')
            return redirect('registerUser')
    else:
        form = UserForm()

    context = {
        'form':form,
    }
    return render(request,'accounts/registerUser.html',context)
