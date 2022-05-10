from pyexpat import model
from django.contrib import admin
from .models import Destination, Bus
# Register your models here.
admin.site.register(Destination)
admin.site.register(Bus)
