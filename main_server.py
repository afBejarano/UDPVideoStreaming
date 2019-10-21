import os
import subprocess 
import socket 
import json

initial_port = 65123
proc = []

with open("cred.json", 'r') as cred:
    data = json.loads(cred.read())
    usrs = data.get('usrs')
    keys = data.get('keys')

for x in os.listdir("video1"):
    os.system("server {} \"video1/{}\"".format(initial_port,x))
    initial_port += 1

s = socket.socket()         
host = socket.gethostname() 
port = 12345
s.bind((host, port))

f = open('video1/test{}.mp4'.format(len(os.listdir("video1"))),'wb')
s.listen(5)                 
while True:
    c, addr = s.accept()    
    usr = c.recv(1024).decode('utf-8')
    key = c.recv(1024).decode('utf-8')
    if usr not in usrs or key not in keys:
        c.close()
        continue
    c.send('ok'.encode('utf-8'))
    print('Got connection from', addr)
    print("Receiving...")
    l = c.recv(1024)
    while (l):
        print("Receiving...")
        f.write(l)
        l = c.recv(1024)
    f.close()
    print( "Done Receiving")
    c.close()
    os.system("server {} \"video1/{}\"".format(initial_port,len(os.listdir("video1"))-1))
    initial_port += 1