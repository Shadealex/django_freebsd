#-*-coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

# Create your models here.

# class Statistic(models.Model):
	# pass

	# def __unicode__(self):
		# return self.name

class Verify_type(models.Model):
	name = models.CharField(verbose_name = _('Название'), max_length=255)
	visibility = models.BooleanField(verbose_name = _('Статус'), default=True, db_index=True)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['name']
		db_table = 'verify_type'
		verbose_name = _("Тип проверки")
		verbose_name_plural = _("Типы проверок")

class Server(models.Model):
	name = models.TextField(verbose_name = _('Имя сервера'))
	ip = models.GenericIPAddressField(protocol='both', verbose_name = _('IP сервера'))
	date_add = models.DateField(auto_now_add=False, verbose_name = _('Дата добавления'))
	date_edit = models.DateField(auto_now=False, verbose_name = _('Дата редактирования'))
	verify = models.ManyToManyField(Verify_type, related_name='servers', verbose_name = _('Проверки'), blank=True)
	on_off = models.BooleanField(verbose_name = _('Включение'))
	comment = models.TextField(verbose_name = _('Комментарий'))

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['name']
		db_table = 'servers'
		verbose_name = _("Сервер")
		verbose_name_plural = _("Сервера")