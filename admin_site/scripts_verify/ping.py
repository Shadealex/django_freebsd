#!/usr/local/bin/python
# coding: utf-8

import os.path, sys, django, datetime, os, subprocess, pexpect
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
# from catalog.models import Channel
# from users.models import User
# from stats.models import ChannelCurrent, ChannelArchive, DeviceStat
# import redis

# ping = os.popen("sudo /sbin/ping -i 1.0 -c 3 -W1000 sex.com")
# result=subprocess.call(["ping",'-n','1', str(address)],shell=True,stdout=subprocess.PIPE)
# tracert = pexpect.spawn('sudo traceroute -I -4 -w 0.5 ' + host)
host = Server.objects.filter(verify__name='ping')
for x in host:
	print (x.ip)

	ping = pexpect.spawn('ping -c 1 -W1000 %s' % x.ip).readlines()
	print (type(ping[-1].split()[-3].decode('utf-8')))

	if ping[-1].split()[-3].decode('utf-8') == '100%':
		print (ping[0].split()[1].decode('utf-8'))
		print(dir(x))
		res = {
			# 'host':
		}
	# res = {
	# 	'host':ping[0].split()[1].decode('utf-8'),
	# 	'ip': ping[0].split()[2].decode('utf-8'),
	# 	'loss': ping[4].split()[6].decode('utf-8')
	# }
	# print(res)
