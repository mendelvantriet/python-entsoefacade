from django.core import serializers
from django.http import HttpResponse

from .models import Transmission


def index(request):
    items = Transmission.objects.all()
    data = serializers.serialize('json', items)
    return HttpResponse(data, content_type='application/json')
