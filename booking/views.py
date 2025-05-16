from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Room, Hotel, Booking
from .forms import BookingForm, CustomUserCreationForm

def home(request):
    return render(request, 'booking/home.html')

def room_list(request):
    rooms = Room.objects.select_related('hotel').all()
    hotels = Hotel.objects.all()

    hotel_id = request.GET.get('hotel')
    room_type = request.GET.get('type')
    available = request.GET.get('available')
    city = request.GET.get('city')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if hotel_id and hotel_id != "All Hotels":
        rooms = rooms.filter(hotel_id=hotel_id)
    if room_type and room_type != "Room Type":
        rooms = rooms.filter(room_type__icontains=room_type)
    if available == 'true':
        rooms = rooms.filter(available=True)
    elif available == 'false':
        rooms = rooms.filter(available=False)
    if city and city != "All Cities":
        rooms = rooms.filter(hotel__location__icontains=city)
    if min_price:
        try:
            rooms = rooms.filter(price__gte=int(min_price))
        except ValueError:
            pass
    if max_price:
        try:
            rooms = rooms.filter(price__lte=int(max_price))
        except ValueError:
            pass

    cities = hotels.values_list('location', flat=True).distinct()
    paginator = Paginator(rooms, 8)
    page = request.GET.get('page')
    rooms = paginator.get_page(page)

    return render(request, 'booking/room_list.html', {
        'rooms': rooms,
        'hotels': hotels,
        'cities': cities,
    })

@login_required(login_url='login')
def book_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.room = room
            booking.save()
            room.available = False
            room.save()
            return render(request, 'booking/booking_success.html')
    else:
        form = BookingForm(initial={'room': room})
    
    return render(request, 'booking/book_room.html', {'form': form, 'room': room})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('room_list')
    else:
        form = AuthenticationForm()
    return render(request, 'booking/login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'booking/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def user_profile(request):
    bookings = Booking.objects.filter(user=request.user).select_related('room', 'room__hotel')
    return render(request, 'booking/user_profile.html', {'bookings': bookings})

from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booking.room.available = True  # Mark the room as available
    booking.room.save()
    booking.delete()  # Remove the booking
    messages.success(request, "Your booking has been successfully canceled.")
    return HttpResponseRedirect(reverse('profile'))

