from django.contrib import admin

from .models import Shift, AttendanceRecord
admin.site.register(Shift)
admin.site.register(AttendanceRecord)