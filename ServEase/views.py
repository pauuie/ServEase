from django.shortcuts import render, redirect
from .models import *
from .forms import BookingForm, CreateAccountForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.info(request, 'Username Or Password is incorrect')

    return render(request, 'pages/login.html')

def logout_view(request):
    logout(request)
    return redirect ('login')


def home(request):
    return render(request, 'pages/homepage.html')


def about(request):
    return render(request, 'pages/aboutpage.html')


@allowed_users(allowed_roles={'booking'})
def bookingform(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookings')
    context = {'form': form}
    return render(request, 'pages/bookingform.html', context)

                            #bookings

@allowed_users(allowed_roles={'booking'})
def bookings(request):
    bookings = Booking.objects.all()
    total_bookings = bookings.count()

    context = {
       'bookings':bookings,
       'total_bookings':total_bookings
   }
    return render(request, 'pages/bookingpage.html', context)

def services(request):
    services = Service.objects.all()
    total_services = services.count()
   
    context = {
       'services':services,
       'total_services':total_services
   }

    return render(request, 'pages/servicespage.html', context)

@login_required(login_url='login')
def update(request, pk):
    booking = Booking.objects.get(id=pk)
    form = BookingForm(instance = booking)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance = booking)
        if form.is_valid():
            form.save()
            return redirect('bookings')
        
    context = {'form': form}
    return render(request, 'pages/bookingform.html', context)

@login_required(login_url='login')
def delete(request, pk):
    booking = Booking.objects.get(id=pk)
    if request.method == 'POST':
        booking.delete()
        return redirect('bookings')
    
    context = {'booking':booking}
    return render(request, 'pages/delete.html', context)

@unauthenticated_user
def register(request):
    form = CreateAccountForm()
    if request.method == 'POST':
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group =  Group.objects.get(name='booking')
            user.groups.add(group)
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    context = {'form':form}

    return render(request, 'pages/register.html', context)


def profile_view(request):

    return render(request, 'pages/profilepage.html')


