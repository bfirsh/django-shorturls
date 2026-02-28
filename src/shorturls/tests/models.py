"""
A handful of test modules to test out resolving redirects.
"""

from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        app_label = 'shorturls'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/animal/{self.id}/'


class Vegetable(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        app_label = 'shorturls'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'http://example.net/veggies/{self.id}'


class Mineral(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        app_label = 'shorturls'

    def __str__(self):
        return self.name
