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
]


urlpatterns += staticfiles_urlpatterns()