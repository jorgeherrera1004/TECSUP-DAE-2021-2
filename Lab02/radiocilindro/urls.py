from django.urls import path
from . import views

appname = 'ejercicios'

urlpatterns = [
    path('',views.index,name='index'),
    path('respuesta',views.respuesta,name='respuesta'),
]