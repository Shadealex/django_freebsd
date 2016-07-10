from django.contrib import admin
from stat_verify.models import Statistic

# Register your models here.


class StatisticAdmin(admin.ModelAdmin):
	list_display = ['name', 'type_verify', 'date_verify', 'status_verify']
	list_filter = ['name', 'type_verify', 'date_verify']
	search_fields = ['name']

admin.site.register(Statistic, StatisticAdmin)