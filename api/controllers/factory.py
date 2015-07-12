from django.http import HttpResponseRedirect, HttpResponse, Http404, QueryDict

from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist

from jsonview.decorators import json_view

from utilities.services import factory_service

import json

@json_view
def generic (request):
  if request.method == 'GET':
    factory_list = factory_service.getAll()
    json_data = serializers.serialize("json", factory_list)
    status = 200
  elif request.method == 'POST':
    request_post = None

    if request.body != 'None':
      request_post = json.loads(request.body.decode())

    factory = factory_service.create(request_post)
    json_data = serializers.serialize("json", [factory])
    struct = json.loads(json_data)
    json_data = json.dumps(struct[0]) # unwrap from array
    status = 201

  return HttpResponse(json_data, content_type='application/json', status=status)

@json_view
def detail (request, factory_id):
  factory_id = factory_id.encode('ascii', 'ignore')
  try:
    if request.method == 'GET':
      factory = factory_service.getOne(factory_id)
      json_data = serializers.serialize("json", [factory])
      status = 200
    elif request.method == 'PUT':
      request_put = None

      if request.body != 'None':
        request_put = json.loads(request.body.decode())
      factory = factory_service.update(factory_id, request_put)

      json_data = serializers.serialize("json", [factory])
      status = 202
    elif request.method == 'DELETE':
      factory_service.delete(factory_id)
      json_data = json.dumps({"success": "Factory: " + factory_id + " has been deleted."})
      status = 204
      return HttpResponse(json_data, content_type='application/json', status=status)

  except ObjectDoesNotExist:
    raise Http404('Factory with id ' + factory_id + ' does not exist')

  struct = json.loads(json_data)
  json_data = json.dumps(struct[0]) # unwrap from array
  return HttpResponse(json_data, content_type='application/json', status=status)
