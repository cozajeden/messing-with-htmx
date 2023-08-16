from django.urls import path
from . import views

app_name = 'first_steps'

urlpatterns = [
    path('', views.name_list, name='name_list'),
    path('list/', views.list, name='list'),
    path('list/add', views.create, name='list_add'),
    path('delete/<str:name>', views.delete, name='list_delete'),
]