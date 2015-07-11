from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse, Http404

from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse

from utilities.services import factory_service

def showAll (request):
  if request.method == 'GET':
    latest_factory_list = factory_service.getAll()
    context = {'latest_factory_list': latest_factory_list}
    return render(request, 'factory/showAll.html', context)

def showOne (request, factory_id):
  try:
    if request.method == 'GET':
      factory = factory_service.getOne(factory_id)
      return render(request, 'factory/showOne.html', {'factory': factory})
  except ObjectDoesNotExist:
    raise Http404('Factory with id ' + factory_id + ' does not exist')

def create (request):
  if request.method == 'GET':
    return render(request, 'factory/create.html')
  elif request.method == 'POST':
    factory = factory_service.create(request.POST)

    return HttpResponseRedirect(reverse('webapp:factory.showOne', args=(factory.id,)))

def update (request, factory_id):
  try:
    if request.method == 'GET':
      factory = factory_service.getOne(factory_id)
      return render(request, 'factory/update.html', {'factory': factory})
    elif request.method == 'POST':
      factory = factory_service.update(factory_id, request.POST)
      return HttpResponseRedirect(reverse('webapp:factory.showOne', args=(factory.id,)))
  except ObjectDoesNotExist:
    raise Http404('Factory with id ' + factory_id + ' does not exist')

def delete (request, factory_id):
  try:
    factory_service.delete(factory_id)
    return HttpResponseRedirect(reverse('webapp:factory.showAll'))
  except ObjectDoesNotExist:
    raise Http404('Factory with id ' + factory_id + ' does not exist')

