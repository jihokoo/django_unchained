from django.db import models

class Factory(models.Model):
  name = models.CharField(max_length=50)
  email = models.CharField(max_length=50)
  address = models.ForeignKey("Address")
  tags = models.ManyToManyField("Tag")

  def __str__(self):
    return self.name

class Address(models.Model):
  line_1 = models.CharField(max_length=50)
  line_2 = models.CharField(max_length=50)
  city = models.CharField(max_length=50)
  state = models.CharField(max_length=2)
  zipcode = models.CharField(max_length=5)

  def __str__(self):
    return self.line_1

class Tag(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name
