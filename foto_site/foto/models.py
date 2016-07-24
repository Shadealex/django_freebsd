# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

# Create your models here.

class foto(models.Model):
	name = models.CharField(verbose_name = _('Название'), max_length=50, help_text =_('Название фотошрафии'))
	photo = models.ImageField()


	def __str__(self):
		return self.name

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['name']
		db_table = 'pictures'
		verbose_name = _("картинка")
		verbose_name_plural = _("картинки")
