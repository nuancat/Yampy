# -*- coding: utf-8 -*-
import PyQt4.QtGui
from socket import *
import threading

try:
    socket = socket(AF_INET, SOCK_STREAM)
    socket.bind(("", 13196))
    socket.listen(254)
except error:
    print u'Запущена копия программы, либо текущий порт уже занят, сорян'
    sys.exit()

users = dict()
hello = str(raw_input("Your name: "))
socket.sendto("W%HelloRequest%W" + hello, ("192.168.0.255", 13196))

def receiver():
    while True:
        data, address = socket.recvfrom(555)
        if "W%HelloRequest%W" in data and hello not in data:
            print "New participant: " + data[16:]
            users[address[0]] = data[16:]
            socket.sendto("W%HelloRequACK%W" + hello, address)
            continue

        if "W%HelloRequACK%W" in data and hello not in data:
            print "Here is: " + data[16:] + " ("+str(address[0])+")"
            users[address[0]] = data[16:]
            continue

        if address[0] in users.keys():
            print users[address[0]] + ":>>> " + str(data)

def transceiver():
    while True:
        message = str(raw_input())
        socket.sendto(message, ("192.168.0.255", 13196))

rec = threading.Thread(target=receiver)
rec.start()
tran = threading.Thread(target=transceiver)
tran.start()


