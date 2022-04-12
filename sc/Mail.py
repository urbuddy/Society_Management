import random

from django.core.mail import send_mail

from SCM import settings


def send_otp(email):
    user_otp = random.randint(10000, 99999)
    mess = f"Hello {email}, \n Your OTP is {user_otp} \n Thank You"
    # send_mail('OTP request', '<gmail id>', [user.email], fail_silently=False, html_message=mess)
    email_from = settings.EMAIL_HOST_USER
    send_mail('OTP request', mess, email_from, [email], fail_silently=False)
    return user_otp