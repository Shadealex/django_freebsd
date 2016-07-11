#!/usr/local/bin/python
# coding: utf-8

import os.path, sys, django, datetime, pexpect
from time import strptime, mktime, localtime

path = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
if not path in sys.path:
	sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.settings'
django.setup()

from settings import settings
from django.utils.timezone import utc
from main.models import Server, Verify_type
from stat_verify.models import Statistic

host = Server.objects.filter(verify__name='ping')
ver = Verify_type.objects.get(name='ping')
for x in host:
	# print (ver)

	ping = pexpect.spawn('ping -c 1 -W1000 %s' % x.ip).readlines()
	# print (ping[-2].split()[-5].decode('utf-8'))

	if ping[-2].split()[-5].decode('utf-8') == '100%':
		result = Statistic(
			status_verify=str(ping[-2].split()[-5].decode('utf-8')),
			name = x,
			type_verify = ver,
			)
		result.save()
		continue
	result = Statistic(
		status_verify=str(ping[-2].split()[-5].decode('utf-8')),
		name = x,
		type_verify = ver,
		)
	result.save()