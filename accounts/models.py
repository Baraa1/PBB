from django.contrib.auth.models import AbstractUser
from django.db import models
from locations.models import Terminal

##################################################################
###################### 1ST Migration Steps #######################
##################################################################

#### After the 1st migration remove GROUPS blank and null = True
#### Create locations
#### Create your admin user
#### Make your admin a super user
#### assign the super user account a group


# changes these fields built-in behavior
AbstractUser._meta.get_field('first_name').blank = False
AbstractUser._meta.get_field('first_name').null = False

AbstractUser._meta.get_field('last_name').blank = False
AbstractUser._meta.get_field('last_name').null = False

AbstractUser._meta.get_field('email')._unique = True
AbstractUser._meta.get_field('email').blank = False
AbstractUser._meta.get_field('email').null = False

AbstractUser._meta.get_field('groups').blank = False
AbstractUser._meta.get_field('groups').null = False

class CustomUser(AbstractUser, models.Model):
    pass
    # Username, Email, Password, first name, Last name, groups(role) are predefined attributes inherited using ((pass))
    user_id  = models.CharField(max_length=50, blank=False, null=False, unique=True)
    location = models.ForeignKey(Terminal, on_delete=models.SET_NULL, blank=False, null=True)

    def __str__(self):
        return self.username
