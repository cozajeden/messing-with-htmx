from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from . import models
from math import ceil
import logging


per_page = 10

@require_http_methods(['GET'])
def name_list(request):
    return render(request, 'first_steps/name_list.html')

@require_http_methods(['GET'])
def search_element(request, page=1, name=''):
    return render(request, 'first_steps/components/search_element.html', {
        'page': page,
        'name': name,
    })

@require_http_methods(['GET'])
def name_page(request, page=1, name=''):
    names = models.Name.objects.order_by('name')
    if name: names = names.filter(name__icontains=name)
    page = min(page, ceil(names.count() / per_page))
    return render(request, 'first_steps/components/names.html', {
        'objects': names[(page - 1) * per_page:page * per_page],
    })

@require_http_methods(['GET'])
def page_numbers(request, name=''):
    names = models.Name.objects.all()
    if name: names = names.filter(name__icontains=name)
    return render(request, 'first_steps/components/page_numbers.html', {
        'pages': range(1, ceil(names.count() / per_page) + 1),
        'name': name,
    })

@require_http_methods(['GET'])
def list(request, page=1):
    name = request.GET.get('name', '')
    return render(request, 'first_steps/components/list.html', {
        'title': 'List of names',
        'page': page,
        'name': name,
        })