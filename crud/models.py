from django.db import models

class Address(models.Model):
  address_1 = models.CharField(max_length=50)
  address_2 = models.CharField(max_length=50)
  city = models.CharField(max_length=50)
  state = models.CharField(max_length=2)
  zipcode = models.CharField(max_length=5)

  def __str__(self):
    return self.address_1

class Factory(models.Model):
  address = models.ForeignKey(Address)
  name = models.CharField(max_length=50)
  email = models.CharField(max_length=50)

  def __str__(self):
    return self.name
