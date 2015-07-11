from django.http import HttpResponseRedirect, HttpResponse, Http404

from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist

from utilities.services import factory_service

def generic (request):
  if request.method == 'GET':
    factory_list = factory_service.getAll()
    json_data = serializers.serialize("json", factory_list)
  elif request.method == 'POST':
    factory = factory_service.create(request.POST)
    json_data = serializers.serialize("json", factory)

  return HttpResponse(json_data, content_type='application/json')

def detail (request, factory_id):
  try:
    if request.method == 'GET':
      factory = factory_service.getOne()
      json_data = serializers.serialize("json", factory)
    elif request.method == 'PUT':
      factory = factory_service.update(factory_id, request.POST)
      json_data = serializers.serialize("json", factory)
    elif request.method == 'DELETE':
      factory_service.delete(factory_id, request.POST)
      json_data = serializers.serialize("json", {"success": "Factory: " + factory_id + " has been deleted."})
  except ObjectDoesNotExist:
    raise Http404('Factory with id ' + factory_id + ' does not exist')

  return HttpResponse(json_data, content_type='application/json')
