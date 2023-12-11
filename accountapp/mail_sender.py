from django.contrib import messages
from django.core.mail import send_mail
import uuid
from django.conf import settings


from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User, auth
from django.http import request







def send_forget_password_mail(email, token):
    # token = str(uuid.uuid4())
    subject = "https://www.topprojectworld.com  Forget password OTP"
    message = f"Hi , you requested to change your password in www.topprojectworld.com and the required OTP is {token}"  
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,message,email_from,recipient_list)
    return True



