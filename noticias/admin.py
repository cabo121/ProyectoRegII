from django.contrib import admin
from .models import deportes, nacionales, corona

model = deportes, nacionales, corona

admin.site.register(model)