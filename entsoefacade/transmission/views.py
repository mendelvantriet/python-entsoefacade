import json
from datetime import datetime

from django.core.paginator import Paginator
from django.db.models import Sum
from django.db.models.functions import Trunc
from django.http import HttpResponse
from django.shortcuts import render

from .models import Transmission

per_page = 25


def index(request):
    items = Transmission.objects.all()

    paginator = Paginator(items, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'index.html', context=context)


def search(request):
    country_from = request.GET.get('from', '')
    country_to = request.GET.get('to', '')
    start = request.GET.get('start', '')
    end = request.GET.get('end', '')

    items = Transmission.objects.annotate(hour=Trunc('timestamp', 'hour')) \
        .values('country_code_from', 'country_code_to', 'hour') \
        .annotate(Sum('capacity')) \
        .order_by('hour')

    if country_from:
        items = items.filter(country_code_from=country_from)
    if country_to:
        items = items.filter(country_code_to=country_to)
    if start:
        start_date = datetime.strptime(start, '%Y%m%d')
        items = items.filter(timestamp__date__gte=start_date)
    if end:
        end_date = datetime.strptime(end, '%Y%m%d')
        items = items.filter(timestamp__date__lte=end_date)

    data = json.dumps(list(items), default=str)
    return HttpResponse(data, content_type='text')
