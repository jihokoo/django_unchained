from django.test import TestCase

from django.core.urlresolvers import reverse

from utilities.models.factory import Factory
from utilities.models.address import Address
from utilities.models.tag import Tag

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


class FactoryViewTests(TestCase):
    def test_showAll_view_with_no_factories(self):
        response = self.client.get(reverse('webapp:factory.showAll'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['factory_list'], [])

    def test_showAll_view_with_a_factory(self):
        create_factory()
        response = self.client.get(reverse('webapp:factory.showAll'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['factory_list'],
            ['<Factory: Makersrow>']
        )

    def test_showOne_view_with_no_factory(self):
        response = self.client.get(reverse('webapp:factory.showOne', args=(1,)))
        self.assertEqual(response.status_code, 404)

    def test_showOne_view_with_a_factory(self):
        factory = create_factory()
        response = self.client.get(reverse('webapp:factory.showOne', args=(factory.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context['factory'].name,
            factory.name
        )

    def test_create_view(self):
        response = self.client.get(reverse('webapp:factory.create'))
        self.assertEqual(response.status_code, 200)

    def test_create_form_submit(self):
        response = self.client.post(reverse('webapp:factory.create'), {
            'line_1': '495 Ninth Ave',
            'line_2': 'Apt 3C',
            'city': 'New York',
            'state': 'NY',
            'zipcode': '10018',
            'name': 'Shoptiques',
            'email': 'shoptiques@gmail.com'
        })

        self.assertEqual(response.status_code, 302)
        response = self.client.get(response['Location'])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context['factory'].name,
            'Shoptiques'
        )

    def test_update_view_with_nonexistant_factory(self):
        response = self.client.get(reverse('webapp:factory.update', args=(1,)))
        self.assertEqual(response.status_code, 404)

    def test_update_view(self):
        factory = create_factory()
        response = self.client.get(reverse('webapp:factory.update', args=(factory.id,)))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context['factory'].name,
            factory.name
        )

    def test_update_form_submit_with_nonexistant_factory(self):
        response = self.client.post(reverse('webapp:factory.update', args=(1,)))
        self.assertEqual(response.status_code, 404)

    def test_update_form_submit(self):
        factory = create_factory()
        response = self.client.post(reverse('webapp:factory.update', args=(factory.id,)), {
            'line_1': '495 Ninth Ave',
            'line_2': 'Apt 3C',
            'city': 'New York',
            'state': 'NY',
            'zipcode': '10018',
            'name': 'Changed',
            'email': 'changed@gmail.com'
        })

        self.assertEqual(response.status_code, 302)

        response = self.client.get(response['Location'])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context['factory'].id,
            factory.id
        )

        self.assertEqual(
            response.context['factory'].name,
            'Changed'
        )

    def test_delete_submit_with_nonexistant_factoryId(self):
        response = self.client.post(reverse('webapp:factory.delete', args=(1,)))

        self.assertEqual(response.status_code, 404)

    def test_delete_submit(self):
        factory = create_factory()
        response = self.client.post(reverse('webapp:factory.delete', args=(factory.id,)))

        self.assertEqual(response.status_code, 302)

        response = self.client.get(response['Location'])
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['factory_list'], [])
