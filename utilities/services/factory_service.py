from django.core.urlresolvers import reverse
from django.db import IntegrityError

from ..models import Factory, Address, Tag

def getAll ():
  latest_factory_list = Factory.objects.order_by('name')
  return latest_factory_list

# factory_id: string
def getOne (factory_id):
  try:
    factory = Factory.objects.get(id = factory_id)
    return factory
  except Factory.DoesNotExist:
    raise

# factory_id: string, factory_data: QuerySet
def create (factory_data):
  address = Address(
    line_1 = factory_data['line_1'],
    line_2 = factory_data.get('line_2', None),
    city = factory_data['city'],
    state = factory_data['state'],
    zipcode = factory_data['zipcode']
  )
  address.save()

  factory = Factory(
    name = factory_data['name'],
    email = factory_data['email'],
    address = address,
  )
  factory.save()

  tags = factory_data.get('tags', 0)
  if tags != 0:
    tags = tags.split(',')
    for name in tags:
      name = name.lower()
      try:
        tag = Tag(name=name)
        tag.save()
      except IntegrityError as e:
        if 'unique constraint' in e.message.lower():
          tag = Tag.objects.get(name=name)
      factory.tags.add(tag)

  return factory

# factory_id: string, factory_data: QuerySet
def update (factory_id, factory_data):
  try:
    factory = Factory.objects.get(id = factory_id)
  except Factory.DoesNotExist:
    raise

  address = factory.address
  address.line_1 = factory_data['line_1']
  address.line_2 = factory_data.get('line_2', None)
  address.city = factory_data['city']
  address.state = factory_data['state']
  address.zipcode = factory_data['zipcode']
  address.save()

  tags = factory_data.get('tags', 0)
  if tags != 0:
    tags = tags.split(',')
    for name in tags:
      name = name.lower()
      try:
        tag = Tag(name = name)
        tag.save()
        factory.tags.add(tag)
      except IntegrityError as e:
        if 'unique constraint' in e.message.lower():
          tag = Tag.objects.get(name = name)
          for existing in factory.tags.all():
            try:
              if (tags.index(existing.name.encode('ascii', 'ignore'))):
                factory.tags.add(tag)
            except ValueError:
              continue

  factory.name = factory_data['name']
  factory.email = factory_data['email']
  factory.save()

  return factory

# factory_id: string
def delete (factory_id):
  try:
    factory = Factory.objects.get(id = factory_id)
    factory.delete()
  except Factory.DoesNotExist:
    raise
