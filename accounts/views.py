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
            # what ever data we have in form will be assigned to user  
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)
            user.role = User.CUSTOMER
            # save the modified user 
            user.save()
            return redirect('registerUser')
    else:
        form = UserForm()

    context = {
        'form':form,
    }
    return render(request,'accounts/registerUser.html',context)
