import json
from json import load
from typing import ValuesView
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, response, HttpResponseRedirect
from django.template import loader
from .forms import UploadFileForm, ParametersFileForm
from django.conf import settings
from os.path import dirname, isfile, realpath

from .models import *

def index(request):
    #response = "<a href='/dashboard'>Dashboard</a></br><a href='/devices'>Devices</a></br><a href='/devicetypes'>Device Types</a></br><a href='/departments'>Departments</a></br><a href='/measurements'>Measurements</a>"
    context = {"teste" : "teste"}
    template = loader.get_template('smhapp/index.html')
    return HttpResponse(template.render(context, request))

def dashboard(request):
    form = UploadFileForm()
    context = {"form" : form}
    template = loader.get_template('smhapp/dashboard.html')
    return HttpResponse(template.render(context, request))

def devices(request):
    departments = Department.objects.all()
    devicetypes = DeviceType.objects.all()

    context = {
        "departments": departments, 
        "deviceTypes": devicetypes
    }
    
    template = loader.get_template('smhapp/devices.html')
    return HttpResponse(template.render(context, request))

def devicetypes(request):
    formP = ParametersFileForm()
    context = {"formP" : formP}
    template = loader.get_template('smhapp/deviceTypes.html')
    return HttpResponse(template.render(context, request))

def departments(request):
    context = {}
    template = loader.get_template('smhapp/departments.html')
    return HttpResponse(template.render(context, request))

def rooms(request):
    context = {}
    template = loader.get_template('smhapp/rooms.html')
    return HttpResponse(template.render(context, request))

def users(request):
    context = {}
    template = loader.get_template('smhapp/users.html')
    return HttpResponse(template.render(context, request))

def load_rooms(request):
    department_id = request.GET.get('department_id')
    rooms = Room.objects.filter(department_id=department_id)
    context = {"rooms": rooms}
    template = loader.get_template('smhapp/loads/load_rooms.html')
    return HttpResponse(template.render(context, request))

def load_devices(request):
    devices = Device.objects.all()

    context = {
        "devices": devices
    }

    template = loader.get_template('smhapp/loads/load_devices.html')
    return HttpResponse(template.render(context, request))

def create_device(request):
    name = request.POST.get('name')
    model = request.POST.get('model')
    deviceType = request.POST.get('deviceType_id')
    room = Room.objects.get(id=request.POST.get('room_id'))

    device = Device(name=name, code=name+model+str(room.id), model=model, deviceType_id=deviceType, room=room)
    device.save()
    return HttpResponse(200)

def remove_device(request):
    device = Device.objects.get(id=request.POST.get('id'))
    device.delete()
    
    return HttpResponse(200)

def edit_device(request):
    device = Device.objects.get(id=request.POST.get('id'))
    device.name = request.POST.get('name')
    device.model = request.POST.get('model')
    device.deviceType = DeviceType.objects.get(id=request.POST.get('deviceType_id'))
    device.room = Room.objects.get(id=request.POST.get('room_id'))
    device.save()
    
    return HttpResponse(200)

def ArquivoMedicaoView(request):
    if request.method == 'POST':
        date = timezone.now()
        forma = UploadFileForm(request.POST, request.FILES)
        if forma.is_valid():
            for chunk in request.FILES['file'].chunks():
                f = json.loads(chunk)
        selecionada = Device.objects.get(code = f['dispositivo'])
        medicao = Measurement(date=date, device=selecionada)
        medicao.save()
        for key, v in f.items():
            if type(v) == type(1.0):
                value = MeasurementValue(value=v, measurement = medicao, parameter = Parameter.objects.get(code = key))
            else:
                value = MeasurementValue(config=v, measurement = medicao, parameter = Parameter.objects.get(code = key))
            value.save()
        #enviar = Measurement.objects.get(device=selecionada)
    else:
        forma = UploadFileForm()
    return render(request, 'smhapp/dashboard.html', {'medicao': medicao, 'valores': f})

def NewDeviceType(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        devType = DeviceType(name=name)
        devType.save()
        
        formP = ParametersFileForm(request.POST, request.FILES)
        if formP.is_valid():
            for chunk in request.FILES['file'].chunks():
                d = str(chunk).split(', ')
            d.pop()
            d.pop(0)
        for a in d:
            parameter = Parameter(name = a, code = a, deviceType = devType)
            parameter.save()
    else:
        form = UploadFileForm()
    #return render(request, 'smhapp/dashboard.html', {'forma': f})
    return render(request, 'smhapp/arquivoMedicao.html', {'form': d})