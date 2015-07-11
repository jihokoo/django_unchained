from django.db import models
from .address import Address
from .tag import Tag

class Factory(models.Model):
  name = models.CharField(max_length=50)
  email = models.CharField(max_length=50)
  address = models.ForeignKey(Address)
  tags = models.ManyToManyField(Tag, blank=True)

  def __str__(self):
    return self.name

  def stringify_tags(self):
    tags = []
    for tag in self.tags.all():
      tags.append(tag.name.encode('ascii', 'ignore'))
    return ','.join(tags)
