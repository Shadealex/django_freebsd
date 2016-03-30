from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

# Create your models here.
class Server(models.Model):
	name = models.TextField(_('Имя сервера'))
	ip = models.GenericIPAddressField(protocol='both', related_name=_('IP сервера'))
	date_add = models.DateField(auto_now_add=False, related_name=_('Дата добавления'))
	date_edit = models.DateField(auto_now=False, related_name=_('Дата редактирования'))
	verify = models.ManyToManyField(Verify_type, related_name='servers')
	on_off = models.BooleanField(related_name=_('Включение'))
	comment = models.TextField(related_name=_('Комментарий'))

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['order_num']
		db_table = 'servers'
		verbose_name = _("Сервер")
		verbose_name_plural = _("Сервера")

# class Statistic(models.Model):
	# pass

	# def __unicode__(self):
		# return self.name

class Verify_type(models.Model):
	name = models.CharField(related_name=_('Название'), max_length=255)
	visibility = models.BooleanField(related_name=_('Статус'), default=True, db_index=True)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['order_num']
		db_table = 'verify_type'
		verbose_name = _("Проверка")
		verbose_name_plural = _("Проверки")