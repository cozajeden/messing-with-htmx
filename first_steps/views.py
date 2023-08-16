from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.utils import IntegrityError
from django.views.decorators.http import require_http_methods
from django.db import transaction
from . import models
from math import ceil
from typing import List
import logging


per_page = 10

def calculate_pages(names, page: int) -> List[int]:
    """Calculate pages for pagination."""
    pages_count = ceil(names.count() / per_page)
    page = max(page, 5)
    first_page = max(min(page - 3, pages_count - 7), 1)
    last_page = min(pages_count, page + 5)
    pages = set(range(first_page, last_page))
    pages.add(1)
    pages.add(pages_count)
    return sorted(pages)
    

@require_http_methods(['GET'])
def name_list(request):
    """Main view"""
    names = models.Name.objects.order_by('name')
    return render(request, 'first_steps/name_list.html', {
        'pages': calculate_pages(names, 1),
        'objects': names[:per_page],
        'page': 1,
    })

@require_http_methods(['GET'])
def list(request):
    """List of names (HTML component)"""
    name = request.GET.get('name', '')
    page = int(request.GET.get('page', 1))
    names = models.Name.objects.order_by('name')
    if name: names = names.filter(name__icontains=name)
    page = max(min(page, ceil(names.count() / per_page)), 1)
    return render(request, 'first_steps/components/list.html', {
        'objects': names[(page - 1) * per_page:page * per_page],
        'pages': calculate_pages(names, page),
        'page': page,
        'name': name,
        })

@require_http_methods(['POST'])
def create(request):
    name = request.POST.get('add-name', '')
    try:
        if name: models.Name.objects.create(name=name)
    except IntegrityError:
        logging.warning(f'Name {name} already exists')
    return redirect(reverse('first_steps:list') + '?' + request.body.decode('utf-8'))

@require_http_methods(['DELETE'])
@transaction.atomic
def delete(request, name):
    models.Name.objects.filter(name=name).delete()
    request.method = 'GET'
    query_params = request.body.decode('utf-8').split('&')
    request.GET = {param.split('=')[0]: param.split('=')[1] for param in query_params if param}
    return list(request)
