from django.conf.urls import url
from django.urls import path
from .views import *

app_name = 'code_generator'

urlpatterns = [
    path('index/', index, name="index"),
    path('logout/', logout, name="logout"),
    path('create_code/', create_code, name="create_code"),
    path('search_code/', search_code, name="search_code"),
    path('update_code/', update_code, name="update_code"),
    path('delete_code/', delete_code, name="delete_code"),
    path('create_code/<int:field_number>/', create_code, name="create_code"),
    path('search_code/<int:field_number>/', search_code, name="search_code"),
    path('update_code/<int:field_number>/', update_code, name="update_code"),
    path('delete_code/<int:field_number>/', delete_code, name="delete_code"),
    url('404/', handler404),
    url('500/', handler500),

]