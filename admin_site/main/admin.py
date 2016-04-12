#-*-coding: utf-8 -*-
from django.contrib import admin
from main.models import Verify_type, Server, Statistic

# Register your models here.
class Verify_typeAdmin(admin.ModelAdmin):
	list_display = ['name', 'visibility', 'comment']
	list_filter = ['visibility']
	search_fields = ['name']

admin.site.register(Verify_type, Verify_typeAdmin)

class ServerAdmin(admin.ModelAdmin):
	list_display = ['name', 'ip', 'date_add', 'date_edit', 'on_off', 'comment']
	list_filter = ['name', 'ip', 'verify', 'on_off']
	search_fields = ['name', 'ip']

admin.site.register(Server, ServerAdmin)

class StatisticAdmin(admin.ModelAdmin):
	list_display = ['name', 'type_verify', 'date_verify', 'status_verify']
	list_filter = ['name', 'type_verify', 'date_verify']
	search_fields = ['name']

admin.site.register(Statistic, StatisticAdmin)