from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_str  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .token import account_activation_token  
from django.contrib.auth.models import User  
from django.core.mail import EmailMessage 
from django.http import HttpResponse  
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
def send_mail(user):  

            # to get the domain of the current site 
             
            user = User.objects.get(username=user)
            current_site = Site.objects.get_current().domain
            print(user)
            print(current_site)
            #current_site = get_current_site(request)  
            mail_subject = 'Activation link has been sent to your email id'  
            message = render_to_string('acc_active_email.html', {  
                'user': user,  
                'domain': 'http://localhost:8000',  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
            })  
            to_email = 'siddharam125@gmail.com'  
            email = EmailMessage(  
                        mail_subject, message, to=[to_email]  
            )  
            email.send()  
             
     