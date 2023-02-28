#!/usr/bin/python

#
# Simple HTTP Server
# Jesus M. Gonzalez-Barahona
# jgb @ gsyc.es
# TSAI and SAT subjects (Universidad Rey Juan Carlos)
# September 2010
# September 2009
# Febraury 2022


import socket
import random
import sys

# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', int(sys.argv[1])))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTLM page
#  (in a loop)
primera_peticion = True

while True:
    print("Waiting for connections")
    (recvSocket, address) = mySocket.accept()
    print("HTTP request received:")
    received = recvSocket.recv(2048)
    print(received)

    recibido = received.decode()
    peticion = recibido.split(" ")[1][1:] #Me quedo con la peticion hecha al servidor

    peticion_lista = peticion.split("/")

    if peticion == "favicon.ico":
        resultado = "No favicons for now"
    else:
        if primera_peticion:
            operando1 = int(peticion)
            primera_peticion = False
            resultado = "Falta un segundo operador."
        else:
            operando2 = int(peticion)
            primera_peticion = True
            resultado = "Resultado: " + str(operando1 + operando2)


    """operacion = peticion_lista[1]
    operando1 = int(peticion_lista[2])
    operando2 = int(peticion_lista[3])

    if operacion == "sumar":
        resultado = operando2 + operando1
    elif operacion == "restar":
        resultado = operando2 - operando1
    elif operacion == "multiplicar":
        resultado = operando2 * operando1
    elif operacion == "dividir":
        resultado = (operando2 / operando1)"""


    aleatorio = random.randint(1,10000)

    response = "HTTP/1.1 200 OK\r\n\r\n" \
            + "<html><body><h1>Hello World! <br>"\
            + "<h2>Eres el usuario con direccion: " + address[0] + "<br>"\
            + "</h1>" \
            + "<a href=http://localhost:"+sys.argv[1]+"/"+str(aleatorio)+"> enlace aleatorio <br><a/>"\
            + "peticion de recurso: " + peticion + "<br>"\
            + "<img src= 'http://gsyc.es/logo.gif'/> <br>"\
            + str(resultado) + "<br>"\
            + "</body></html>"\
            + "\r\n"
    recvSocket.send(response.encode('utf-8'))
    recvSocket.close()