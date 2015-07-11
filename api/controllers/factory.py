from django.http import HttpResponseRedirect, HttpResponse, Http404

from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist

from utilities.services import factory_service

import json

def generic (request):
  if request.method == 'GET':
    factory_list = factory_service.getAll()
    json_data = serializers.serialize("json", factory_list)
  elif request.method == 'POST':
    factory = factory_service.create(request.POST)
    json_data = serializers.serialize("json", [factory])
    struct = json.loads(json_data)
    json_data = json.dumps(struct[0])

  return HttpResponse(json_data, content_type='application/json')

def detail (request, factory_id):
  factory_id = factory_id.encode('ascii', 'ignore')
  try:
    if request.method == 'GET':
      factory = factory_service.getOne(factory_id)
      json_data = serializers.serialize("json", [factory])
    elif request.method == 'PUT':
      factory = factory_service.update(factory_id, request.POST)
      json_data = serializers.serialize("json", [factory])
    elif request.method == 'DELETE':
      factory_service.delete(factory_id)
      json_data = serializers.serialize("json", [{"success": "Factory: " + factory_id + " has been deleted."}])
  except ObjectDoesNotExist:
    raise Http404('Factory with id ' + factory_id + ' does not exist')

  struct = json.loads(json_data)
  json_data = json.dumps(struct[0])
  return HttpResponse(json_data, content_type='application/json')
