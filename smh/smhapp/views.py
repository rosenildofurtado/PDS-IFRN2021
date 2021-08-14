from genericpath import isfile
import json
from json import load
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, response, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .forms import UploadFileForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
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
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            for chunk in request.FILES['file'].chunks():
                f = json.loads(chunk)
    else:
        form = UploadFileForm()
    #return render(request, 'smhapp/dashboard.html', {'forma': f})
    return render(request, 'smhapp/arquivoMedicao.html', {'form': f})
    