from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import ViewModel

# Register your models here.

class ViewModelAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email",)


admin.site.register(ViewModel, ViewModelAdmin)
