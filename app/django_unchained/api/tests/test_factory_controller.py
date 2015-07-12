from django.test import TestCase

from django.core.urlresolvers import reverse

from utilities.models.factory import Factory
from utilities.models.address import Address
from utilities.models.tag import Tag

import json

def create_factory():
    a1 = Address.objects.create(
      line_1 = '495 Ninth Ave',
      line_2 = 'Apt 3C',
      city = 'New York',
      state = 'NY',
      zipcode = '10018'
    )
    f1 = Factory.objects.create(
      name = 'Makersrow',
      email = 'makersrow@gmail.com',
      address = a1,
    )
    return f1


class FactoryControllerTests(TestCase):

    def test_getAll_with_no_factories(self):
        response = self.client.get(reverse('api:factory.generic'), None, 'json')
        self.assertEqual(response.status_code, 200)
        json_string = response.content
        data = json.loads(json_string)
        self.assertQuerysetEqual(data, [])

    def test_getAll_with_a_factory(self):
        factory = create_factory()
        response = self.client.get(reverse('api:factory.generic'), None, 'json')
        self.assertEqual(response.status_code, 200)
        json_string = response.content
        data = json.loads(json_string)

        factory = Factory.objects.get(id=factory.id)
        self.assertEqual(
            data[0]['fields']['name'],
            factory.name
        )

    def test_getOne_with_no_factory(self):
        response = self.client.get(reverse('api:factory.detail', args=(1,)), None, 'json')
        self.assertEqual(response.status_code, 404)

    def test_getOne_with_a_factory(self):
        factory = create_factory()
        response = self.client.get(reverse('api:factory.detail', args=(factory.id,)), None, 'json')
        self.assertEqual(response.status_code, 200)

        json_string = response.content
        data = json.loads(json_string)

        self.assertEqual(
            data['fields']['name'],
            factory.name
        )

    def test_create_factory(self):
        response = self.client.post(reverse('api:factory.generic'), json.dumps({
            'line_1': '495 Ninth Ave',
            'line_2': 'Apt 3C',
            'city': 'New York',
            'state': 'NY',
            'zipcode': '10018',
            'name': 'Shoptiques',
            'email': 'shoptiques@gmail.com',
        }), 'json')

        self.assertEqual(response.status_code, 201)

        json_string = response.content
        data = json.loads(json_string)

        self.assertEqual(
            data['fields']['name'],
            'Shoptiques'
        )

    def test_update_with_nonexistant_factory(self):
        response = self.client.put(reverse('api:factory.detail', args=(1,)), None, 'json')
        self.assertEqual(response.status_code, 404)

    def test_update(self):
        factory = create_factory()
        response = self.client.put(reverse('api:factory.detail', args=(factory.id,)), json.dumps({
            'line_1': '495 Ninth Ave',
            'line_2': 'Apt 3C',
            'city': 'New York',
            'state': 'NY',
            'zipcode': '10018',
            'name': 'Changed',
            'email': 'changed@gmail.com',
        }), 'json')

        self.assertEqual(response.status_code, 202)

        json_string = response.content
        data = json.loads(json_string)

        self.assertEqual(
            data['pk'],
            factory.id
        )

        self.assertEqual(
            data['fields']['name'],
            'Changed'
        )

    def test_delete_with_nonexistant_factoryId(self):
        response = self.client.delete(reverse('api:factory.detail', args=(1,)), None, 'json')
        self.assertEqual(response.status_code, 404)

    def test_delete(self):
        factory = create_factory()
        response = self.client.delete(reverse('api:factory.detail', args=(1,)), None, 'json')
        self.assertEqual(response.status_code, 204)
