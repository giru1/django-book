from django.http import HttpResponse
from .models import Bb


def index(request):
    s = 'List board'
    for item in Bb.objects.order_by('-published'):
        s += ' ' + item.title + ' '
    return HttpResponse(s+'11111111', content_type='text/plain; charset=utf-8')
