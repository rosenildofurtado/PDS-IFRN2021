from genericpath import isfile
import json
from json import load
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, response, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core import serializers
from .forms import UploadFileForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.files import File
from os.path import dirname, isfile, realpath

from .models import *


# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            #handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def simple_upload(request):
    if request.method == 'POST' and request.FILES['arquivo']:
        myfile = request.FILES['arquivo']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'smhapp/arquivoMedicao.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'smhapp/arquivoMedicao.html')

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
    context = {}
    template = loader.get_template('smhapp/devices.html')
    return HttpResponse(template.render(context, request))

def devicetypes(request):
    context = {}
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

def ArquivoMedicaoView(request):

    if request.method == 'POST' and request.FILES['file']:
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        #arq = open(uploaded_file_url)
        with open('smhapp/parametros.json') as f:
            data = load(f)
        return render(request, 'smhapp/arquivoMedicao.html', {
            'uploaded_file_url': data
        })
    return render(request, 'smhapp/arquivoMedicao.html')

    f=""
    s=""
    if(request.method == 'POST'): 
        form = UploadFileForm(request.POST,request.FILES)
    else:
        form = UploadFileForm()
        f = request.FILES['arquivo']
        
        for qn in f.chunks():
            s = qn
    
    #a = file.read()
    
    v = '{"dispositivo":"pc1","momentoMedicao":"06-07-2021-15-06-54","modelo":"lenovoS145","mac":"031da5003a34","ip":"10.32.0.145","processador":"ryzen5","memoriaRAM":12,"discoHD":1000,"discoSSD":256,"cpu":45.7,"ram":66.8,"hd":16.4,"ssd":56.1,"temperaturaCPU":45,"up":5.6,"down":27.9}'
    
    #f = json.loads(v)
    #a = serializers.deserialize("json", v)
        #context = {'teste': fileRead, 'tamanho':tam}
    context = {'form': f}
    return render(request, 'smhapp/arquivoMedicao.html', context)
        #return HttpResponseRedirect(reverse('enquetes:resultado', args=(pergunta_id,)))
        #return HttpResponseRedirect(reverse('enquetes:arquivoMedicao', args=(arq)))
    #return render(request, 'enquetes/arquivoMedicao.html', context)
        #return HttpResponse(file)
    #context = {}
    #template = loader.get_template('smhapp/arquivoMedicao.html')
    #for i, item in enumerate(v):
    #    v[i] = json.loads(item)
    #return HttpResponse(template.render(context, request))
    #fileRead = file[0].read()
    #tam = file.size
    #f = file.read()
    #a=open('smhapp/parametros.json')
    #f = json.dump(file[0])
    #with file.open() as f:
    #texto = request.POST['arq']
        #arq = open(str(texto))
    #file = request.POST['arquivo']