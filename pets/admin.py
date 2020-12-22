from django.contrib import admin

# Register your models here.

from .models import Owner, Pet

# Register your models here.
admin.site.register(Owner)
admin.site.register(Pet)