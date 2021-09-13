from django.contrib import admin

from .models import Department, DeviceType, Device, User, Room, Measurement, MeasurementValue, Parameter

admin.site.register(Department)
admin.site.register(DeviceType)
admin.site.register(Device)
admin.site.register(User)
admin.site.register(Room)
admin.site.register(Measurement)
admin.site.register(Parameter)
admin.site.register(MeasurementValue)