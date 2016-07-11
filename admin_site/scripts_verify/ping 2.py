#!/usr/local/bin/python

import sys
import time
import os

ip = sys.argv[1]

ping = os.popen("sudo /sbin/ping -i 1.0 %s" %ip) 
packetlost = 0
prev_id = 0 
while 1:
    try:
        line = ping.readline()
        filter_line = line.split()[4][9:]
        now_id = int(filter_line)

        if (now_id == prev_id + 1) or (prev_id == 0):
            prev_id = now_id
            continue

        timelost = time.ctime()
        packetlost = now_id - prev_id 
        print "[%s] %s Lost %s packets" %(ip, time.strftime("%H:%M:%S"), packetlost)
        prev_id = now_id
    except:
        pass

    if not line:
        break
