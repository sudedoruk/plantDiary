from django.urls import path
from .views import *

urlpatterns = [

    path('index',plant_index),
    path('delete',plant_delete),
    path('detail',plant_detail),
    path('update',plant_update),
    path('create',plant_create),

]
