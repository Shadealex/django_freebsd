from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from main.models import Server, Verify_type

# Create your models here.
class Statistic(models.Model):
	name = models.ForeignKey(Server, verbose_name=_('Имя сервера'))
	type_verify = models.ForeignKey(Verify_type, verbose_name=_('Название теста'))
	date_verify = models.DateTimeField(verbose_name = _('Дата проверки'),auto_now_add=True)
	status_verify = models.CharField(verbose_name = _('Результат'), max_length=100)

	def __repr__(self):
		return self.name

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['name']
		db_table = 'Statistics'
		verbose_name = _('Статистику')
		verbose_name_plural = _('Статистика')