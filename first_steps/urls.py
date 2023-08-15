from django.urls import path
from . import views

app_name = 'first_steps'

urlpatterns = [
    path('', views.name_list, name='name_list'),
    path('name-page/<int:page>/', views.name_page, name='name_page'),
    path('name-page/<int:page>/<str:name>/', views.name_page, name='name_page_filtered'),
    path('list/', views.list, name='list'),
    path('list/<int:page>/', views.list, name='list_paged'),
    path('page-numbers/', views.page_numbers, name='page_numbers'),
    path('page-numbers/<str:name>', views.page_numbers, name='page_numbers_filtered'),
    path('search-element/<int:page>/', views.search_element, name='search_element'),
    path('search-element/<int:page>/<str:name>/', views.search_element, name='search_element_filtered'),
]