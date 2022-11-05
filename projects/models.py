from django.db import models

class Company(models.Model):
  company_name=models.CharField(max_length=255)

  class Meta:
    ordering = ['company_name']
  def __str__(self):
    return self.company_name

class Person(models.Model):
  full_name=models.CharField(max_length=255)
  phone_number=models.CharField(max_length=255, null=True)
  birthday = models.DateField(null=True)
  company_name=models.ManyToManyField(Company)
  class Meta:
    ordering = ['full_name']

  def __str__(self):
    return self.full_name

