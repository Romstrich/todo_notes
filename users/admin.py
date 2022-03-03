from django.contrib import admin

# Register your models here.
from .models import User


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    fields = ('username','first_name','last_name','email')
    list_display = ('username','first_name','last_name','email')
