from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse

from django.core.urlresolvers import reverse

from .models import Factory, Address

def showAll (request):
  if request.method == 'GET':
    latest_factory_list = Factory.objects.order_by('name')
    context = {'latest_factory_list': latest_factory_list}
    return render(request, 'factory/showAll.html', context)

def showOne (request, factory_id):
  if request.method == 'GET':
    factory = get_object_or_404(Factory, id=factory_id)
    return render(request, 'factory/showOne.html', {'factory': factory})


def create (request):
  if request.method == 'GET':
    return render(request, 'factory/create.html')
  elif request.method == 'POST':
    address = Address(
      line_1 = request.POST["line_1"],
      line_2 = request.POST["line_2"],
      city = request.POST["city"],
      state = request.POST["state"],
      zipcode = request.POST["zipcode"]
    )
    address.save()

    factory = Factory(
      name = request.POST["name"],
      email = request.POST["email"],
      address = address,
    )
    factory.save()

    return HttpResponseRedirect(reverse('factory:showOne', args=(factory.id,)))

def update (request, factory_id):
  factory = get_object_or_404(Factory, id=factory_id)

  if request.method == 'GET':
    return render(request, 'factory/update.html', {'factory': factory})
  elif request.method == 'POST':

    address = factory.address
    address.line_1 = request.POST["line_1"]
    address.line_2 = request.POST["line_2"]
    address.city = request.POST["city"]
    address.state = request.POST["state"]
    address.zipcode = request.POST["zipcode"]
    address.save()

    factory.name = request.POST["name"]
    factory.email = request.POST["email"]
    factory.save()

    return HttpResponseRedirect(reverse('factory:showOne', args=(factory.id,)))

def delete (request, factory_id):
  get_object_or_404(Factory, id=factory_id).delete()
  return HttpResponseRedirect(reverse('factory:showAll'))

