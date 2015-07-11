from django.db import models

class Factory(models.Model):
  name = models.CharField(max_length=50)
  email = models.CharField(max_length=50)
  address = models.ForeignKey("Address")
  tags = models.ManyToManyField("Tag", blank=True)

  def __str__(self):
    return self.name

  def stringify_tags(self):
    tags = []
    for tag in self.tags.all():
      tags.append(tag.name.encode('ascii', 'ignore'))
    return ','.join(tags)

class Address(models.Model):
  line_1 = models.CharField(max_length=50)
  line_2 = models.CharField(max_length=50, blank=True)
  city = models.CharField(max_length=50)
  state = models.CharField(max_length=2)
  zipcode = models.CharField(max_length=5)

  def __str__(self):
    return self.line_1

class Tag(models.Model):
  name = models.CharField(max_length=50, unique=True)

  def __str__(self):
    return self.name
