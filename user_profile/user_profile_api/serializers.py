from .models import UserProfile, UserGroup
# from django.contrib.auth.models import Group, User
from rest_framework import serializers


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['firstname', 'lastname', 'username', 'email', 'is_privileged', 'is_active']


class UserGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserGroup
        fields = ['group_name', 'group_members', 'group_owner_email']