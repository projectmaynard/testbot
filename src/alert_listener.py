# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 21:59:54 2017

@author: hamish.mogan
"""

import socket
import sys

 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port

def start_alert_listener(in_q):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
    #Bind socket to local host and port
#    try:
    server_address=(HOST,PORT)
    sock.bind(server_address)
    sock.listen(1)
    print('Socket now listening')
    
    #now keep talking with the client
    while 1:
        #wait to accept a connection - blocking call
        conn, addr = sock.accept()
        print('@@@@@@@@@@: Connected with ' + addr[0] + ':' + str(addr[1]))
        data = conn.recv(1024)
        print('@@@@@@@@@@###: Message: ' + data.decode('utf-8'))
         
        #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
        #start_new_thread(clientthread ,(conn,))
 
    sock.close()
 
#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
    conn.send('Welcome to the server. Type something and hit enter\n') #send only takes string
     
    #infinite loop so that function do not terminate and thread do not end.
    while True:
         
        #Receiving from client
        data = conn.recv(1024)
        reply = 'OK...' + data
        if not data: 
            break
     
        conn.sendall(reply)
     
    #came out of loop
    conn.close()
 
