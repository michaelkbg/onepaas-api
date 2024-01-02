from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class UserProfile(models.Model):
    firstname = models.CharField(max_length=80)
    lastname = models.TextField(max_length=80)
    username = models.TextField(max_length=80)
    email = models.TextField(max_length=200)
    is_privileged = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.firstname
 
# Create User Group Model
class UserGroup(models.Model):
    group_name = models.CharField(max_length=100)
    group_members = ArrayField(models.CharField(max_length=200), blank=True)
    group_owner_email = models.EmailField(max_length=200)
    
    def __str__(self):
        return self.group_name
