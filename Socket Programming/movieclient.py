from pydoc import cli
from secrets import choice
import socket
import sys

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP,PORT)
FORMAT = "utf-8"
SIZE = 1024
a = 1

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
        client.connect(ADDR)
except socket.error as e:
        print(str(e))

print(client.recv(SIZE).decode(FORMAT))
print(client.recv(SIZE).decode(FORMAT))
#enter the name
name = input()
client.send(name.encode(FORMAT))
#choose date
print(client.recv(SIZE).decode(FORMAT))
#enter the date
date = input()
client.send(date.encode(FORMAT))
#choose place
print(client.recv(SIZE).decode(FORMAT))
choice1 = input()
client.send(choice1.encode(FORMAT))
#choose mall
print(client.recv(SIZE).decode(FORMAT))
choice2 = input()
client.send(choice2.encode(FORMAT))
#choose movie
print(client.recv(SIZE).decode(FORMAT))
choice3 = input()
client.send(choice3.encode(FORMAT))
#no of seats
print(client.recv(SIZE).decode(FORMAT))
avai_seat = client.recv(SIZE).decode(FORMAT)
print(avai_seat)
# print(type(avai_seat))
# print(client.recv(SIZE).decode(FORMAT))
# no of seats

choice4 = input()
client.send(choice4.encode(FORMAT))
if choice4.isnumeric()== False:
    print(client.recv(SIZE).decode(FORMAT))
    choice4 = input()
    client.send(choice4.encode(FORMAT))

choice5 = -1
while((str(choice4) < '0' or str(choice4) > avai_seat)and(str(choice5) < '0' or str(choice5) > avai_seat)):
    print(client.recv(SIZE).decode(FORMAT))
    choice5 = input()
    client.send(choice5.encode(FORMAT))

print(client.recv(SIZE).decode(FORMAT))
choice6 = input()
client.send(choice6.encode(FORMAT))
# filename = (client.recv(SIZE).decode(FORMAT))
# ticket = open("clientdata/"+filename,'w+')
# data = client.recv(SIZE).decode(FORMAT)
# ticket.write(data)
# print(data)
if(choice6 == 'yes'):
    print(client.recv(SIZE).decode(FORMAT))
    print(client.recv(SIZE).decode(FORMAT))
    print(client.recv(SIZE).decode(FORMAT))
    print(client.recv(SIZE).decode(FORMAT))
    print(client.recv(SIZE).decode(FORMAT))
    print(client.recv(SIZE).decode(FORMAT))
    print(client.recv(SIZE).decode(FORMAT))
    print(client.recv(SIZE).decode(FORMAT))
else:
    print(client.recv(SIZE).decode(FORMAT))

# ticket.close()
client.close()

# client.send(data.encode(FORMAT))
# msg = client.recv(SIZE).decode(FORMAT)
# print(f"[SERVER]: {msg}")


