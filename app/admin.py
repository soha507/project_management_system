from django.contrib import admin

# Register your models here.


# from socket import SOL_NETROM
import unittest.util
from django.db import models
#
# Create your models here.
from .models import appointment,contact
admin.site.register(appointment)
admin.site.register(contact)
