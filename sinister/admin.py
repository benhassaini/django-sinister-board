from django.contrib import admin

# Register your models here.
from .models import Sinister,Category

admin.site.register(Sinister)
admin.site.register(Category)