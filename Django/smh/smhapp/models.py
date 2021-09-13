from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    shortName = models.CharField(max_length=50,null=True,blank=True)
    description = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        if self.shortName:
            return self.shortName
        else:
            return self.name

    def getDepartment(departmentId):
        department = Department.objects.get(pk=departmentId)
        return department

class DeviceType(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete = models.PROTECT)

class Room(models.Model):
    name = models.CharField(max_length=100)
    shortName = models.CharField(max_length=50,null=True,blank=True)
    description = models.CharField(max_length=200,null=True,blank=True)
    department = models.ForeignKey(Department, on_delete = models.PROTECT)

    def __str__(self):
        if self.shortName:
            return self.shortName
        else:
            return self.name
    
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

    def __str__(self):
        return self.name + " (" + self.room.name + ")"

class Measurement(models.Model):
    date = models.DateTimeField('Momento da medição')
    device = models.ForeignKey(Device, on_delete = models.PROTECT)

class Parameter(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)
    text = models.BooleanField(default=False)
    dangerUpAlarm = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    dangerDownAlarm = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    warningUpAlarm = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    warningDownAlarm = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    deviceType = models.ForeignKey(DeviceType, on_delete = models.CASCADE)

    def __str__(self):
        return self.name + " (" + self.code + ")"

class MeasurementValue(models.Model):
    value = models.CharField(max_length=50)
    measurement = models.ForeignKey(Measurement, on_delete = models.CASCADE)
    parameter = models.ForeignKey(Parameter, on_delete = models.PROTECT)