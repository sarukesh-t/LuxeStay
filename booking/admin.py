from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Hotel, Room

admin.site.register(Hotel)
admin.site.register(Room)
