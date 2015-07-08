from django.shortucts import render

from .models import Factory

def index (request):
  latest_factory_list = Factory.objects.order_by('name')
  context = {'latest_factory_list': latest_factory_list}
  return render(request, 'crud/index.html', context)
