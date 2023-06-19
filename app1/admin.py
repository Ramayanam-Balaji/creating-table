from django.contrib import admin

# Register your models here.
from app1.models import *
admin.site.register(Dept)
admin.site.register(Emp)
