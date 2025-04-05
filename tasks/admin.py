from django.contrib import admin
from .models import Task
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'user', 'description')
    search_fields = ('name', 'description')
    list_filter = ('status',)

admin.site.register(Task, TaskAdmin)
