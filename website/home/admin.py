from django.contrib import admin

from .models import UserPhoto
from .models import Appointment
from .models import AvailableTime


admin.site.register(UserPhoto)
admin.site.register(Appointment)
admin.site.register(AvailableTime)
