from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

def detectUser(user):
    if user.role == 1:
        redirectUrl = 'vendorDashboard'
    elif user.role== 2:
        redirectUrl = 'custDashboard'
    elif user.role == None and user.is_superadmin:
        redirectUrl = '/admin'
        return redirectUrl
    
    # Helper function to send verification email 

def send_verification_email(request,user):
    current_site = get_current_site(request)
    mail_subject = 'Please activate your account'
    # message body 
    message = render_to_string('accounts/emails/accounts_verification.html',{
        'user':user,
        'domain':current_site,
        # send encoded uid and send it into email body
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),    
        # make_token=>creates the token 
        'token':default_token_generator.make_token(user),      
    })
    to_email = user.email
    mail = EmailMessage(mail_subject,message,to = [to_email])
    mail.send()