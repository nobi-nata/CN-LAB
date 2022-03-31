import socket
# uses ipv4 formate,SOCK_STREAM uses tcp for udp SOCK_DGRAM
c= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    c.connect(('localhost',1800))
except socket.error as e:
    print(str(e))
print(c.recv(1024).decode())
print(c.recv(1024).decode())
name=input()
c.send(bytes(name,'utf-8'))
print(c.recv(1024).decode())

print(c.recv(1024).decode())
mob=(input())
c.send(bytes(mob,'utf-8'))
print(c.recv(1024).decode())
date=(input())
c.send(bytes(date,'utf-8'))
print(c.recv(1024).decode())



m_name=input()
c.send(bytes(m_name,'utf-8'))
sig=(c.recv(1024).decode())
print(sig)
if sig=='-1':
    print("Seats are not available for this movie .Thank you for visiting ")
    c.close()
    
    
else:
    print(c.recv(1024).decode())
    s_n=(input())
    c.send(bytes(s_n,'utf-8'))

    print(c.recv(1024).decode())
    print(c.recv(1024).decode())
    c_r=(input())
    c.send(bytes(c_r,'utf-8'))


    if c_r=='1':
        print(c.recv(1024).decode())
        c_n=(input())
        c.send(bytes(c_n,'utf-8'))
        print(c.recv(1024).decode())
        print(c.recv(1024).decode())
       
    else:
        print(c.recv(1024).decode())
        print(c.recv(1024).decode())
        print(c.recv(1024).decode()) 
        c.close()   