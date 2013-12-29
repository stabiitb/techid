from django.db import models

# Create your models here.
from django.contrib.auth.hashers import *
from django.template import RequestContext, loader

from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from misc.models import *
import re
def validate_mobile(mobile):
    pattern = "0?[0-9]{10}"
    return re.match(pattern,mobile)


class UserManager(BaseUserManager):
    def create_user(self,email=None,is_active=None,
    	mobile=None, password=None,first_name=None,last_name=None, **extra_fields):
        if is_active == None:
            is_active = True
        user = self.model(
            email=UserManager.normalize_email(email),
            first_name=first_name or '',
            last_name=last_name or '',
            is_active=is_active,
            mobile = mobile,**extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,  email, password, first_name=None, last_name=None):
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=254, unique=True, db_index=True)
    mobile = models.CharField(max_length=10,null=True,blank=True,
        unique=True,validators=[validate_mobile])
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    department = models.OneToOneField(Department)
    hostel = models.OneToOneField(Hostel)
    year = models.OneToOneField(Year)
    ldap_username = models.CharField(max_length=20,null=True,blank=True)
    rollno=models.CharField(max_length=20,null=True,blank=True)
    alternate_email = models.EmailField(null=True,blank=True)
    room = models.CharField(null=True,blank=True,max_length=10)


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= ['first_name','department','hostel','year','ldap_username']

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.first_name
    
    @property
    def is_staff(self):
        return self.is_admin

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
