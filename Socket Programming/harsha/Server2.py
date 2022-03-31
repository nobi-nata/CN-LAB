
from ctypes import c_size_t
import socket
import os
from _thread import *

ServerSocket = socket.socket()
host = 'localhost'
port = 1800
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(5)
a_seat = 60
b_seat = 60
c_seat = 60
global c_t 
c_t = 0

def threaded_client(c):
    global a_seat
    global b_seat
    global c_seat
    c.send(bytes(f'-------------------------------------------------------\n ','utf-8'))
    c.send(bytes("Welcome to our Movie Booking server of Gopalan Mall\nPlease Enter Your Name:",'utf-8'))
    name=c.recv(1024).decode()
    print(f"connected with {addr,name}")

    c.send(bytes(f'welcome {name}','utf-8'))

    c.send(bytes('Please Enter your Mobile Number:','utf-8'))
    mob=c.recv(1024*5).decode()
    print(mob)
    c.send(bytes('Select Movie Name:\n 1.James 2.RRR 3.Kashmir Files  ','utf-8'))
    global inp
    inp=c.recv(1024).decode()
    

    if inp=='1':
        if a_seat==0:
            c.send(bytes(f'-1' ,'utf-8')) 
            c.close()
           #c.send(bytes(f'Seats are not available for this movie .Thank you for visiting  ' ,'utf-8')) 
        else:
            c.send(bytes(f'Available seats are {a_seat}','utf-8'))
                     
    elif inp=='2':
        if b_seat==0:
           c.send(bytes(f'Seats are not available for this movie .Thank you for visiting ','utf-8')) 
        else:
            c.send(bytes(f'Available seats are {b_seat}','utf-8'))         
    elif inp=='3':
        if c_seat==0:
           c.send(bytes(f'Seats are not available for this movie .Thank you for visiting','utf-8')) 
        else:
           c.send(bytes(f'Available seats are {c_seat}','utf-8'))         
    else:
        c.send(bytes(f'Invalid Input ','utf-8'))
        c.close()         

        


    c.send(bytes('How many seats you want to book: ','utf-8'))
    s_n=int(c.recv(1024).decode())    
    #s_n=2
    

    def book(inp,s_n):
        global a_seat
        global c_seat
        global b_seat
        if inp=='1':
            if (a_seat <= 60 ) and (a_seat-s_n >=0):
                a_seat=a_seat-s_n
                return 1
            else:
               # print("Seats are full ")
                return -1    
            
        elif inp=='2':
           if b_seat <=60 and b_seat-s_n>=0:
                b_seat=b_seat-s_n
                return 1
           else:
               # print("Seats are full ")
                return -1 
         
        elif inp=='3':
            if c_seat <=60 and c_seat-s_n>=0:
                c_seat=c_seat-s_n
                return 1
            else:
               # print("Seats are full ")
                return -1
        else:
           # print("invalid input \n")
            return 0
            
    #c.send(bytes(book(inp,s_n),'utf-8'))
       
    if book(inp,s_n)==1:
        c.send(bytes(f'successfully booked {s_n} tickets  ','utf-8'))
    elif book(inp,s_n)==0:
        c.send(bytes('Invalid input  ','utf-8'))
        c.close()    
    elif book(inp,s_n)==-1:
        c.send(bytes(f'Seats are full ,Thank you for visiting','utf-8'))
        c.close()
        

    else:            
        c.send(bytes('Do you want to cancel tickets (yes=1 / No=0)','utf-8'))
        c_r=int(c.recv(1024).decode())
        if c_r==1:
            c.send(bytes(f'How many seats you want to cancel','utf-8'))
            c_t=int(c.recv(1024).decode())

            if c_t<=(s_n) and c_t>=0:
                c.send(bytes(f'{c_t} Tickets are cancelled , {s_n-c_t} are booked and confirmed','utf-8'))
                if inp=='1':
                    a_seat=a_seat+c_t
                elif inp=='2':
                    b_seat=b_seat+c_t   
                else:
                    c_seat=c_seat+c_t     
            else:
                c.send(bytes('Invalid input  ','utf-8'))
                c.close()
        elif c_r==0:
            c.send(bytes(f'{s_n} tickets are booked and confirmed','utf-8'))
            c.send(bytes(f'Booking Information : \n Name: {name} \n No. of seats {s_n-c_t} \n ','utf-8'))
            if inp=='1':
             c.send(bytes(f'Movie Name: James','utf-8'))
            elif inp=='2':
                c.send(bytes(f'Movie Name: RRR','utf-8') )   
            elif inp=='3':
             c.send(bytes(f'Movie Name: Kashmir Files','utf-8') )   


        c.send(bytes(f'Thank you for visiting ','utf-8'))
    
        c.close()




    c.send(bytes('Do you want to cancel tickets (yes=1 / No=0)','utf-8'))
    c_r=int(c.recv(1024).decode())
    if c_r==1:
        c.send(bytes(f'How many seats you want to cancel','utf-8'))
      
        c_t=int(c.recv(1024).decode())
        if c_t<=(s_n) and c_t>=0:
            c.send(bytes(f'{c_t} Tickets are cancelled , {s_n-c_t} are booked and confirmed','utf-8'))
            if inp=='1':
                a_seat=a_seat+c_t
            elif inp=='2':
                b_seat=b_seat+c_t   
            else:
                c_seat=c_seat+c_t     
        else:
            c.send(bytes('Invalid input  ','utf-8'))
            c.close()
    elif c_r==0:
        c.send(bytes(f'{s_n} tickets are booked and confirmed','utf-8'))

    
    c.send(bytes(f'------------------------------------------------------------------------------------------------------\n ','utf-8'))
    c.send(bytes(f'Booking Information : \n Name: {name} \n No.of seats: {s_n-c_t} \n ','utf-8'))
    if inp=='1':
        c.send(bytes(f'Movie Name: James','utf-8'))
    elif inp=='2':
        c.send(bytes(f'Movie Name: RRR','utf-8') )   
    elif inp=='3':
        c.send(bytes(f'Movie Name: Kashmir Files','utf-8') )
    c.send(bytes(f'\n------------------------------------------------------------------------------------------------------\n ','utf-8'))
           
    c.send(bytes(f' Thank you for visiting ','utf-8'))

    c.close()    


while True:
    c, addr = ServerSocket.accept()
    print('Connected to: ' + addr[0] + ':' + str(addr[1]))
    start_new_thread(threaded_client, (c, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()