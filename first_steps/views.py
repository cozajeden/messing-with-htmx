from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from . import models
from math import ceil
import logging


per_page = 10

@require_http_methods(['GET'])
def name_list(request):
    names = models.Name.objects.order_by('name')
    return render(request, 'first_steps/name_list.html', {
        'title': 'List of names',
        'page': 1,
        'name': '',
        'objects': names[:per_page],
        'pages': range(1, ceil(names.count() / per_page) + 1),
    })

@require_http_methods(['GET'])
def search_element(request):
    name = request.GET.get('name', '')
    page = int(request.GET.get('page', 1))
    return render(request, 'first_steps/components/search_element.html', {
        'name': name,
        'page': page,
    })

@require_http_methods(['GET'])
def name_page(request):
    name = request.GET.get('name', '')
    page = int(request.GET.get('page', 1))
    names = models.Name.objects.order_by('name')
    if name: names = names.filter(name__icontains=name)
    page = min(page, ceil(names.count() / per_page))
    return render(request, 'first_steps/components/names.html', {
        'objects': names[(page - 1) * per_page:page * per_page],
        'page': page,
        'name': name,
    })

@require_http_methods(['GET'])
def page_numbers(request):
    names = models.Name.objects.all()
    name = request.GET.get('name', '')
    page = int(request.GET.get('page', 1))
    if name: names = names.filter(name__icontains=name)
    return render(request, 'first_steps/components/page_numbers.html', {
        'pages': range(1, ceil(names.count() / per_page) + 1),
        'name': name,
        'page': page,
    })

@require_http_methods(['GET'])
def list(request):
    name = request.GET.get('name', '')
    page = int(request.GET.get('page', 1))
    names = models.Name.objects.order_by('name')
    if name: names = names.filter(name__icontains=name)
    page = min(page, ceil(names.count() / per_page))
    return render(request, 'first_steps/components/list.html', {
        'pages': range(1, ceil(names.count() / per_page) + 1),
        'objects': names[(page - 1) * per_page:page * per_page],
        'title': 'List of names',
        'page': page,
        'name': name,
        })