from django.contrib import admin

# Register your models here.

from event.models import *
from signup.models import *

admin.site.register(Student)
