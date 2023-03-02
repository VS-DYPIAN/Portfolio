from django.contrib import admin
from .models import Job
from django.contrib.auth.models import Group, User


   


admin.site.register(Job)
admin.site.unregister(User)
admin.site.unregister(Group)