from django.contrib import admin
from django.urls import path, include
from booking import views as booking_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('booking.urls')),  # ✅ Changed from 'rooms/' to ''
]
