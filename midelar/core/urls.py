from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name ='home'),
    path('arduino/', views.arduino, name = 'arduino'),
    path('circuitos_digitales/', views.circuitos_digitales, name = 'circuitos_digitales'),
    path('raspberry/', views.raspberry, name = 'raspberry'),
    path('python/', views.python, name = 'python'),
    path('store/', views.store, name = 'store'),
]