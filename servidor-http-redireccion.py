#!/usr/bin/python

#
# Simple HTTP Server
# Carlos Nebril Jiménez
# c.nebril.2020 @ alumnos.urjc.es
# URJC
# February 202

import socket
import sys
import random
from craft_popular_urls import url_list

try:
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket.bind(('localhost', int(sys.argv[1])))
except IndexError:
    print("Please, we need at least one argument and it has to be an integer (port).")
    sys.exit(0)

mySocket.listen(5)  # Queue a maximum of 5 TCP connection requests

try:
    while True:
        print("Waiting for connections")
        (recvSocket, address) = mySocket.accept()
        print("HTTP request received:")
        received = recvSocket.recv(2048)  # info in bytes
        print(received)
        r = random.randint(1, 100)
        print(r)

        response = "HTTP/1.1 301 Moved Permanently\r\n" \
                   + "Location: " + str(url_list[r]) + "\r\n\r\n"

        if received != b'' and received.decode().split(" ")[1] == "/favicon.ico":  # .decode() --> transform bytes to string
            pass
        else:
            print(response)
            recvSocket.send(response.encode('utf-8'))
            recvSocket.close()

except KeyboardInterrupt:
    print("Server stopped by the user.")




