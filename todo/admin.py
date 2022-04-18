from django.contrib import admin

# Register your models here.
from todo.models import Project, Todo


@admin.register(Project)
class AdminProject(admin.ModelAdmin):
    fields = ('name', 'users')
    list_display = ('name', 'get_users')


@admin.register(Todo)
class AdminTodo(admin.ModelAdmin):
    fields = ('project',  'created_user', 'active', 'note_text')
    list_display = ('project', 'created_at', 'updated_at', 'created_user', 'active', 'note_text')

