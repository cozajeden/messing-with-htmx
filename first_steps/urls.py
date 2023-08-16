from django.urls import path
from . import views

app_name = 'first_steps'

urlpatterns = [
    path('', views.name_list, name='name_list'),
    path('name-page/', views.name_page, name='name_page'),
    path('list/', views.list, name='list'),
    path('page-numbers/', views.page_numbers, name='page_numbers'),
    path('search-element/', views.search_element, name='search_element'),
]