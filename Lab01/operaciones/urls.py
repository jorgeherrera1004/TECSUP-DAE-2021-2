from django.urls import path
from . import views

urlpatterns = [
    path('suma/<int:var1>/<int:var2>',views.suma,name='suma'),
    path('resta/<int:var1>/<int:var2>',views.resta,name='resta'),
    path('multiplicacion/<int:var1>/<int:var2>',views.multiplicacion,name='resta'),
    path('division/<int:var1>/<int:var2>',views.division,name='division')
]

