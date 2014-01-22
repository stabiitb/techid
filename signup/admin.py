from django.contrib import admin

# Register your models here.

from event.models import *
from signup.models import *
class UserAdmin(admin.ModelAdmin):
	list_display = ['email','first_name','last_name','department','year','mobile','hostel']
	search_fields = ['email','first_name','last_name']

admin.site.register(User,UserAdmin)
admin.site.register(RegistrationCode)
