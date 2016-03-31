#-*-coding: utf-8 -*-
from django.contrib import admin
from main.models import Verify_type, Server

# Register your models here.
class Verify_typeAdmin(admin.ModelAdmin):
	list_display = ['name', 'visibility']
	list_filter = ['visibility']
	search_fields = ['name']

admin.site.register(Verify_type, Verify_typeAdmin)

class ServerAdmin(admin.ModelAdmin):
	list_display = ['name', 'ip', 'date_add', 'date_edit', 'on_off', 'comment']
	list_filter = ['name', 'ip', 'verify', 'on_off']
	search_fields = ['name', 'ip']

admin.site.register(Server, ServerAdmin)