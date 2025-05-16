# booking/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rooms/', views.room_list, name='room_list'),
    path('book/<int:room_id>/', views.book_room, name='book_room'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.user_profile, name='profile'),  # ✅ This must match
    path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]
