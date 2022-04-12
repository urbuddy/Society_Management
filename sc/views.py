import pdb
import random

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist

from SCM import settings
from .forms import NoticeForm, ComplaintForm
from .models import User, Notice, Complaint


def send_otp(email, subject, body):
    # mess = f"Hello {email}, \n Your OTP is {user_otp} \n Thank You"
    # send_mail('OTP request', '<gmail id>', [user.email], fail_silently=False, html_message=mess)
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, body, email_from, [email], fail_silently=False)


def home(request):
    notices = Notice.objects.filter().order_by('-dateTime')
    complaints = Complaint.objects.filter().order_by('-dateTime')
    return render(request, "sc/home.html", {'notices': notices, 'complaints': complaints})


@login_required(login_url='/login')
def add_notice(request):
    if request.method == "POST":
        form = NoticeForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost.save()
            obj = form.instance
            alert = True
            return redirect('home')
    else:
        form = NoticeForm()
    return render(request, "sc/add_notice.html", {'form': form})


@login_required(login_url='/login')
def add_complaint(request):
    if request.method == "POST":
        form = ComplaintForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost.save()
            obj = form.instance
            alert = True
            return redirect('home')
    else:
        form = NoticeForm()
    return render(request, "sc/add_complaint.html", {'form': form})


def profile(request):
    return render(request, "sc/profile.html")


def maintenance(request):
    return render(request, "sc/maintanance.html")


def signup(request):
    try:
        if request.method == "POST":
            email = request.POST['email']
            first_name = request.POST['first']
            last_name = request.POST['last']
            flat_no = request.POST['flat_no']
            mobile_no = request.POST['mobile_no']
            tower_no = request.POST['tower_no']
            password1 = request.POST['password']
            password2 = request.POST['confirm_password']
            if password1 != password2:
                messages.error(request, 'password does not match')
                return redirect('signup')

            user = User.objects.create_user(email, password1)
            user.first_name = first_name
            user.last_name = last_name
            user.flat_no = flat_no
            user.tower_no = tower_no
            user.mobile_no = mobile_no

            user.save()
            '''user_otp = random.randint(10000, 99999)
            mess = f"Hello {user.email}, \n Your OTP is {user_otp} \n Thank You"
            # send_mail('OTP request', '<gmail id>', [user.email], fail_silently=False, html_message=mess)
            email_from = settings.EMAIL_HOST_USER
            send_mail('OTP request', mess, email_from, [user.email], fail_silently=False)'''
            user_otp = random.randint(10000, 99999)
            # b = OTPBlog(otp=OTP, email=email)
            # b.save()
            request.session['email'] = email
            request.session['otp'] = user_otp
            body = 'Hello,\n'+'Your OTP is ' + str(user_otp)
            send_otp(email, 'OTP Verification', body)

            # pdb.set_trace()
            messages.success(request, 'ou must have received a mail. Verify your Id to login')
            return redirect('otp')
    except IntegrityError:
        q = email + ' already exist'
        messages.error(request, q)
    return render(request, "sc/Signup.html")


def otp_verify(request):
    # OTP = send_otp(request.session['email'])
    OTP = request.session['otp']
    if request.method == "POST":

        # po = Status.objects.latest('id')
        # email = request.session['email']
        # pdb.set_trace()
        if OTP == int(request.POST['otp']):
            user = User.objects.get(email=request.session['email'])
            user.is_verified = True
            # pdb.set_trace()
            user.save()
            return redirect('login')
        else:
            messages.error(request, "OTP does not match. recheck or click to resend otp")
            redirect('otp')
    return render(request, 'sc/otp.html')


def Login(request):
    if request.method == "POST":
        emails = request.POST['email']
        password = request.POST['password']
        try:
            usr = User.objects.get(email=emails)
            if usr.is_verified == True:
                user = authenticate(username=emails, password=password)

                if user is not None:
                    login(request, user)
                    messages.success(request, "Successfully Logged In")
                    return redirect("/")
                else:
                    messages.error(request, "Invalid Credentials")
            else:
                messages.warning(request, "Please verify your account, Register Again!")
                usr.delete()
                redirect('sc/signup')
        except User.DoesNotExist:
            messages.error(request, "Invalid Credentials,You needs to create your account")
            redirect('sc/signup')
    return render(request, "sc/login.html")


'''def email_message(email_to, subject, body):
    email_from = settings.EMAIL_HOST_USER
    print('Hello', email_to, subject, body)
    send_mail(subject, body, email_from, [email_to], fail_silently=False)
    return True'''


def Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('login')
