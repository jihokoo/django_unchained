from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse


from .models import Factory

def index (request):
  latest_factory_list = Factory.objects.order_by('name')
  context = {'latest_factory_list': latest_factory_list}
  return render(request, 'factory/index.html', context)

def show (request, factory_id):
  factory = get_object_or_404(Factory, id=factory_id)
  return render(request, 'factory/show.html', {'factory': factory})

def new (request):
  return render(request, 'factory/new.html')

def create (request):
  return HttpResponseRedirect(reverse('factory:index'))

def edit (request, factory_id):
  factory = get_object_or_404(Factory, id=factory_id)
  return render(request, 'factory/edit.html', {'factory': factory})

def update (request, factory_id):
  factory = get_object_or_404(Factory, id=factory_id)
  return HttpResponseRedirect(reverse('factory:index', args=(factory,)))

