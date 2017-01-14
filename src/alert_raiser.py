# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 22:32:26 2017

@author: hamish.mogan
"""

#!/usr/bin/env python

import socket


TCP_IP = 'localhost'
TCP_PORT = 8888
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE.encode('utf-8'))
s.close()
