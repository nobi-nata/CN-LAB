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
def main():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(ADDR)

    print(client.recv(SIZE).decode(FORMAT))
    print(client.recv(SIZE).decode(FORMAT))
    #enter the name
    name = input()
    client.send(name.encode(FORMAT))
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
    print(client.recv(SIZE).decode(FORMAT))
    print(client.recv(SIZE).decode(FORMAT))
    # no of seats
    # print(client.recv(SIZE).decode(FORMAT))
    choice4 = input()
    client.send(choice4.encode(FORMAT))
    choice5 = 0
    while((choice4 < 0 and choice4 > 100)or(choice5 < 0 and choice4 > 100)):
        print(client.recv(SIZE).decode(FORMAT))
        choice5 = input()
        client.send(choice5.encode(FORMAT))
        
    
    
    
    filename = (client.recv(SIZE).decode(FORMAT))
    ticket = open("clientdata/"+filename,'w+')
    data = client.recv(SIZE).decode(FORMAT)
    ticket.write(data)
    print(data)
    ticket.close()


    # client.send(data.encode(FORMAT))
    # msg = client.recv(SIZE).decode(FORMAT)
    # print(f"[SERVER]: {msg}")

    client.close()

if __name__ == "__main__":
    main()