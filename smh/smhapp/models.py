from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    shortName = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def getDepartment(departmentId):
        department = Department.objects.get(pk=departmentId)
        return department

class DeviceType(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)

class User(models.Model):
    name = models.CharField(max_length=50)
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete = models.PROTECT)

class Room(models.Model):
    name = models.CharField(max_length=100)
    shortName = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete = models.PROTECT)
    
    def create(name, shortName, description, departmentId):
        department = Department.objects.get(pk=departmentId)
        room = department.room_set.create(name = name, shortName = shortName, description = description)
        return room

class Device(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete = models.PROTECT)
    deviceType = models.ForeignKey(DeviceType, on_delete = models.PROTECT)

class Measurement(models.Model):
    date = models.DateTimeField('Momento da medição')
    device = models.ForeignKey(Device, on_delete = models.PROTECT)

class Parameter(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)
    dangerUpAlarm = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    dangerDownAlarm = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    warningUpAlarm = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    warningDownAlarm = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    deviceType = models.ForeignKey(DeviceType, on_delete = models.CASCADE)

class MeasurementVaue(models.Model):
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    measurement = models.ForeignKey(Measurement, on_delete = models.CASCADE)
    parameter = models.ForeignKey(Parameter, on_delete = models.PROTECT)