from django.contrib import admin

# Register your models here.
from .models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ['first_name','last_name','birthdate']
    list_display = ('first_name','last_name','birthdate')

