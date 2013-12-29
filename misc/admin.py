from django.contrib import admin

# Register your models here.
from misc.models import *
admin.site.register(Department)
admin.site.register(Hostel)
admin.site.register(Club)
admin.site.register(Year)
admin.site.register(Venue)
