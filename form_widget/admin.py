from django.contrib import admin

# Register your models here.
from .models import Widget_model
admin.site.register(Widget_model)