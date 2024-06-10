from django.urls import path
from . import views

urlpatterns = [    
    path('index', views.index , name="index"),
    path('crud', views.crud, name='crud'),
    path('alumnosAdd', views.alumnos.Add, name='alumnosAdd'),
    path('alumnos_del/<str:pk>', views.alumnos_del, name='alumnos_del'),
    path('alumnos_finedit/<str:pk>', views.alumnos_finedit, name='alumnos_finedit'),
]