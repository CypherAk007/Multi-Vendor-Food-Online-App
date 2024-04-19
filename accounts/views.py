from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def registeruser(request):
    return render(request,'accounts/registerUser.html')
