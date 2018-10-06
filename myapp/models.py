# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Product(models.Model):
	homepage = models.CharField(max_length=50)
	description = models.CharField(max_length=50)

	def __unicode__(self):
		return self.homepage