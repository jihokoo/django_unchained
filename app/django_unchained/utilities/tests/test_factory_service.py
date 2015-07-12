from django.test import TestCase

from ..models.factory import Factory
from ..models.address import Address
from ..models.tag import Tag

from ..services import factory_service

class FactoryServiceTests(TestCase):

  def setUp(self):
    a1 = Address.objects.create(
      line_1 = '495 Ninth Ave',
      line_2 = 'Apt 3C',
      city = 'New York',
      state = 'NY',
      zipcode = '10018'
    )

    a2 = Address.objects.create(
      line_1 = '400 Broome St.',
      line_2 = 'Apt 5C',
      city = 'New York',
      state = 'NY',
      zipcode = '10013'
    )

    f1 = Factory.objects.create(
      name = 'Makersrow',
      email = 'makersrow@gmail.com',
      address = a1,
    )

    f2 = Factory.objects.create(
      name = 'Shoptiques',
      email = 'shoptiques@gmail.com',
      address = a2,
    )

  def test_get_all_factories(self):
    factory_list = factory_service.getAll()
    self.assertIsInstance(factory_list[0], Factory)
    self.assertIsInstance(factory_list[0].address, Address)
    self.assertIsInstance(factory_list[1], Factory)
    self.assertIsInstance(factory_list[1].address, Address)
    self.assertEqual(factory_list.count(), 2)
    self.assertEqual(factory_list[0].name, 'Makersrow')
    self.assertEqual(factory_list[1].name, 'Shoptiques')

  def test_get_one_factory(self):
    factory = factory_service.getOne(1)
    self.assertEqual(factory.name, 'Makersrow')

  def test_create_factory(self):
    factory = factory_service.create({
      "line_1": '35 5th Ave.',
      "line_2": 'Apt 8B',
      "city": 'New York',
      "state": 'NY',
      "zipcode": '10005',
      "name": 'Moveline',
      "email": 'moveline@gmail.com',
    })

    self.assertIsInstance(factory, Factory)
    self.assertIsInstance(factory.address, Address)
    self.assertEqual(factory.name, 'Moveline')
    self.assertEqual(factory.email, 'moveline@gmail.com')

    factory_list = factory_service.getAll()
    self.assertEqual(factory_list.count(), 3)

  def test_update_factory(self):
    factory = factory_service.getOne(1)
    self.assertEqual(factory.name, 'Makersrow')

    updated_factory = factory_service.update(factory.id, {
      "line_1": '140 E. 14th St.',
      "line_2": 'Apt 5E',
      "city": 'New York',
      "state": 'NY',
      "zipcode": '10003',
      "name": 'Palladium',
      "email": 'palladium@gmail.com',
    })

    factory_list = factory_service.getAll()
    self.assertEqual(factory_list.count(), 2)

    self.assertEqual(factory.id, updated_factory.id)
    self.assertEqual(updated_factory.name, 'Palladium')

  def test_delete_factory(self):
    factory_list = factory_service.getAll()
    self.assertEqual(factory_list.count(), 2)

    factory_service.delete(factory_list[0].id)
    factory_list = factory_service.getAll()
    self.assertEqual(factory_list.count(), 1)
    self.assertEqual(factory_list[0].name, 'Shoptiques')




