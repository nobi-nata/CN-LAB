from ast import Raise
import socket

# uses ipv4 formate,SOCK_STREAM uses tcp for udp SOCK_DGRAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket created ")
s.bind(('localhost',1800))
s.listen(2)

a_seat=0

c_seat=60
b_seat=60
while True:

    c,addr=s.accept()

    #print(f"connected with {addr}")
    c.send(bytes('welcome to our Movie server ,please enter your name','utf-8'))
    name=c.recv(1024).decode()
    print(f"connected with {addr,name}")

    c.send(bytes(f'welcome {name}','utf-8'))

    c.send(bytes('Please enter your mobile number','utf-8'))
    print(c.recv(1024*5).decode())
    c.send(bytes('Here there are  Movie name select one \n 1.A 2.B 3.C  ','utf-8'))
    inp=c.recv(1024).decode()


    if inp=='1':
        if a_seat==0:
           c.send(bytes(f'Seats are not available for this movie .Thank you for visiting  ' ,'utf-8')) 
           
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

        


    c.send(bytes('How many seats you want to book ','utf-8'))
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
    elif book(inp,s_n)==-1:
        c.send(bytes(f'Seats are full','utf-8'))
    elif book(inp,s_n)==0:
        c.send(bytes('Invalid input  ','utf-8'))        

    c.send(bytes('Do you want to cancel tickets (yes=1/no=0)','utf-8'))
    c_r=int(c.recv(1024).decode())
    if c_r==1:
        c.send(bytes(f'How many seats you want to cancel','utf-8'))
        c_t=int(c.recv(1024).decode())
        if c_t<=(s_n) and c_t<=0:
            c.send(bytes(f'{c_t} Tickets are canceld , {s_n-c_t} are booked and confirmed','utf-8'))
        else:
            c.send(bytes('Invalid input  ','utf-8'))
    elif c_r==0:
        c.send(bytes(f'{s_n} tickets are booked and confirmed','utf-8'))
           

    
    c.send(bytes(f'Thank you for visiting ','utf-8'))
 
    c.close()
