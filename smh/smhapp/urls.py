from django.urls import path

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'smhapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('devices/', views.devices, name='devices'),
    path('devicetypes/', views.devicetypes, name='devicetypes'),
    path('departments/', views.departments, name='departments'),
    path('departments/rooms/', views.rooms, name='rooms'),
    path('users/', views.users, name='users'),

    path('arquivoMedicao/', views.ArquivoMedicaoView, name = 'arquivoMedicao'),
    path('arquivoParametros/', views.NewDeviceType, name = 'arquivoParametros'),

    path('load/load_rooms', views.load_rooms, name='load_rooms'),
    path('load/load_devices', views.load_devices, name='load_devices'),

    path('load/create_device', views.create_device, name='create_device'),   
    path('load/remove_device', views.remove_device, name='remove_device'),   
    path('load/edit_device', views.edit_device, name='edit_device'), 
]


urlpatterns += staticfiles_urlpatterns()