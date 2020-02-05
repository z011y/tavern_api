from django.contrib import admin

from .models import Musician, Venue

# Register your models here.
admin.site.register(Musician)
admin.site.register(Venue)
