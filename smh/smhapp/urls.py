from django.urls import path

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'smhapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('devices/', views.devices, name='devices'),
    path('devicetypes/', views.devicetypes, name='devicetypes'),
    path('departments/', views.departments, name='departments'),
    path('departments/<int:id>/rooms/', views.rooms, name='rooms'),
    path('users/', views.users, name='users'),

    path('arquivoMedicao/', views.ArquivoMedicaoView, name = 'arquivoMedicao'),
    path('arquivoParametros/', views.NewDeviceType, name = 'arquivoParametros'),

    path('load/load_rooms', views.load_rooms, name='load_rooms'),
    path('load/load_departments', views.load_departments, name='load_departments'),
    path('load/load_room_cards', views.load_room_cards, name='load_room_cards'),
    path('load/load_devices', views.load_devices, name='load_devices'),

    path('load/create_device', views.create_device, name='create_device'),   
    path('load/remove_device', views.remove_device, name='remove_device'),   
    path('load/edit_device', views.edit_device, name='edit_device'), 

    path('load/create_department', views.create_department, name='create_department'), 
    path('load/edit_department', views.edit_department, name='edit_department'), 
    path('load/remove_department', views.remove_department, name='remove_department'), 

    path('load/create_room', views.create_room, name='create_room'), 
    path('load/edit_room', views.edit_room, name='edit_room'), 
    path('load/remove_room', views.remove_room, name='remove_room'), 
]


urlpatterns += staticfiles_urlpatterns()