import json
from json import load
from django.utils import timezone
from django.db import connections
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, response, HttpResponseRedirect
from django.template import loader
from .forms import CorrentDeviceType, UploadFileForm, ParametersFileForm
from django.conf import settings
from os.path import dirname, isfile, realpath

from .models import *

def index(request):
    context = {}
    template = loader.get_template('smhapp/index.html')
    return HttpResponse(template.render(context, request))

def login(request):
    context = {}
    template = loader.get_template('smhapp/login.html')
    return HttpResponse(template.render(context, request))

def dashboard(request):
    form = UploadFileForm()
    devicetypes = DeviceType.objects.all()
    
    context = {
        "form": form,
        "deviceTypes": devicetypes
    }
    template = loader.get_template('smhapp/dashboard.html')
    return HttpResponse(template.render(context, request))

def deviceDetails(request, id):
    medicao = Measurement.objects.filter(device = Device.objects.get(pk=id)).order_by('-pk')[0]
    values = MeasurementValue.objects.filter(measurement=medicao)
    return render(request, 'smhapp/deviceDetails.html', {'medicao': medicao, 'valores': values})
   

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
    departments = Department.objects.all()

    context = {
        "departments": departments, 
    }
    template = loader.get_template('smhapp/departments.html')
    return HttpResponse(template.render(context, request))

def rooms(request, id):
    print(id)
    context = {"department_id": id}
    template = loader.get_template('smhapp/rooms.html')
    return HttpResponse(template.render(context, request))

def users(request):
    context = {}
    template = loader.get_template('smhapp/users.html')
    return HttpResponse(template.render(context, request))

def load_dashboard(request):
    deviceType_id = request.GET.get('deviceType_id')
    devices = Device.objects.filter(deviceType_id=deviceType_id)
    parameters = Parameter.objects.filter(deviceType_id=deviceType_id)
    context = {
        "devices": devices,
        "parameters": parameters
    }
    template = loader.get_template('smhapp/loads/load_dashboard.html')
    return HttpResponse(template.render(context, request))

def load_departments(request):
    departments = Department.objects.all()

    context = {
        "departments": departments
    }
    template = loader.get_template('smhapp/loads/load_departments.html')
    return HttpResponse(template.render(context, request))

def load_room_cards(request):
    department_id = request.GET.get('department_id')
    rooms = Room.objects.filter(department_id=department_id)
    context = {"rooms": rooms}
    template = loader.get_template('smhapp/loads/load_room_cards.html')
    return HttpResponse(template.render(context, request));    

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

def create_department(request):
    name = request.POST.get('name')
    shortName = request.POST.get('shortName')
    description = request.POST.get('description')

    department = Department(name=name, shortName=shortName, description=description)
    department.save()
    return HttpResponse(200)

def edit_department(request):
    department = Department.objects.get(id=request.POST.get('id'))
    department.name = request.POST.get('name')
    department.shortName = request.POST.get('shortName')
    department.description = request.POST.get('description')
    department.save()
    
    return HttpResponse(200)

def remove_department(request):
    department = Department.objects.get(id=request.POST.get('id'))
    department.delete()
    
    return HttpResponse(200)

def create_room(request):
    name = request.POST.get('name')
    shortName = request.POST.get('shortName')
    description = request.POST.get('description')

    room = Room(name=name, shortName=shortName, description=description)
    room.save()
    return HttpResponse(200)

def edit_room(request):
    room = Room.objects.get(id=request.POST.get('id'))
    room.name = request.POST.get('name')
    room.shortName = request.POST.get('shortName')
    room.description = request.POST.get('description')
    room.save()
    
    return HttpResponse(200)

def remove_room(request):
    room = Room.objects.get(id=request.POST.get('id'))
    room.delete()
    
    return HttpResponse(200)

def ArquivoMedicaoView(request):
    if request.method == 'POST':
        
        forma = UploadFileForm(request.POST, request.FILES)
        if forma.is_valid():
            for chunk in request.FILES['file'].chunks():
                f = json.loads(chunk)
        date = timezone.now()
        selecionada = Device.objects.get(code = f['dispositivo'])
        medicao = Measurement(date=date, device=selecionada)
        medicao.save()
        values = []
        for key, v in f.items():
            value = MeasurementValue(value=v, measurement = medicao, parameter = Parameter.objects.get(code = key, deviceType = selecionada.deviceType ))
            value.save()
            values.append(value)
    else:
        forma = UploadFileForm()
    return render(request, 'smhapp/deviceDetails.html', {'medicao': medicao, 'valores': values})

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
    return render(request, 'smhapp/deviceDetails.html', {'form': d})