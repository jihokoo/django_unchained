from django.db import models

class Address(models.Model):
  line_1 = models.CharField(max_length=50)
  line_2 = models.CharField(max_length=50, blank=True)
  city = models.CharField(max_length=50)
  state = models.CharField(max_length=2)
  zipcode = models.CharField(max_length=5)

  def __str__(self):
    return self.line_1
