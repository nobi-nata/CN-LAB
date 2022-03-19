from ast import While
from fileinput import filename
from secrets import choice
import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP,PORT)
FORMAT = "utf-8"
SIZE = 1024
PLACES = ['Banashankari','Hoskerahalli']
THETARE = ['Gopalan','Oriean']
MOVIE = ['Kashmir Files','Radhe Shyam','James']
seat11 = 100
seat12 = 100
seat13 = 100
seat21 = 100
seat22 = 100
seat23 = 100



def main():
    print("[STARTING] Server is starting.")
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen(5)
    print("[LISTENING] Server is listening.")
    a = 1
    while True:
        conn,addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")
        str1 = str(a)
        filename = "ticket" + str1 + ".txt"
        a = a + 1
        ticket = open("serverdata/"+filename,'w+')
        
        ticket.write("-----------MOVIE TICKET------------\n")
        conn.send("-------------------LHN MOVIE BOOKING SYSTEM--------------------\n".encode(FORMAT))
        conn.send("Enter Your Name : ".encode(FORMAT))
        name = conn.recv(SIZE).decode(FORMAT)
        ticket.write("Name : "+name+ "\n")
        
        conn.send("Select the place:\n1.Banashankari \n2.Hosekerahalli".encode(FORMAT))
        choice1 = int(conn.recv(SIZE).decode(FORMAT))
        if choice1 == 1:
            ticket.write("Place : Banashankari \n")
            conn.send("Select the theatre:\n1.Gopalan Mall \n2.Orien Mall".encode(FORMAT))
            choice2 = int(conn.recv(SIZE).decode(FORMAT))
            if choice2 == 1:
                ticket.write("Theatre : Gopalan Mall \n")
                conn.send("Select the movie:\n1.Kashmir Files \n2.Radhe Shyam \n3.James".encode(FORMAT))
                choice3 = int(conn.recv(SIZE).decode(FORMAT))
                if choice3 == 1:
                    seat = str(seat13)
                    conn.send("Available Seats: ".encode(FORMAT))
                    conn.send(seat.encode(FORMAT))
                    ticket.write("Movie : Kashmir Files \n")
                    conn.send("\nCost of the ticket : Rs.300/ticket\nEnter the number of seats to be booked:".encode(FORMAT))
                    choice4 = int(conn.recv(SIZE).decode(FORMAT))
                    choice5 = 0
                    while((choice4 < 0 and choice4 > 100)or(choice5 < 0 and choice4 > 100)):
                        conn.send("Enter number within available number of seats:\n".encode(FORMAT))
                        choice5 = int(conn.recv(SIZE).decode(FORMAT))
                    value4 = str(300*choice4)
                    value5 = str(300*choice5)
                    if(choice4 < 0 and choice4 > 100):
                        choice5 = str(choice5)
                        ticket.write("Number of tickets booked: "+choice5+" \n")
                        ticket.write("Cost of " +choice5+ " tickets:"+ value5 +"\n")
                    else:
                        choice4 = str(choice4)
                        ticket.write("Number of tickets booked:"+ choice4+ "\n")
                        ticket.write("Cost of "+choice4+" tickets:"+ value4 +"\n")
                    conn.send("ticket.txt".encode(FORMAT))
                    data = ticket.read()
                    print(data)
                    conn.send(("ticket"+str1+".txt").encode(FORMAT))
                    conn.send(data.encode(FORMAT))
                
                elif choice3 == 2:
                    ticket.write("Movie : Radhe Shyam \n")
                    seat = str(seat13)
                    conn.send("Available Seats: ".encode(FORMAT))
                    conn.send(seat.encode(FORMAT))
                    conn.send("\nCost of the ticket : Rs.300/ticket\nEnter the number of seats to be booked:".encode(FORMAT))
                    
                    choice4 = int(conn.recv(SIZE).decode(FORMAT))
                    choice5 = 0
                    while((choice4 < 0 and choice4 > 100)or(choice5 < 0 and choice4 > 100)):
                        conn.send("Enter number within available number of seats:\n".encode(FORMAT))
                        choice5 = int(conn.recv(SIZE).decode(FORMAT))
                    value4 = str(300*choice4)
                    value5 = str(300*choice5)
                    if(choice4 < 0 and choice4 > 100):
                        choice5 = str(choice5)
                        ticket.write("Number of tickets booked: "+choice5+" \n")
                        ticket.write("Cost of " +choice5+ " tickets:"+ value5 +"\n")
                    else:
                        choice4 = str(choice4)
                        ticket.write("Number of tickets booked:"+ choice4+ "\n")
                        ticket.write("Cost of "+choice4+" tickets:"+ value4 +"\n")
                    # conn.send("ticket.txt".encode(FORMAT))
                    data = ticket.read()
                    print(data)
                    conn.send(data.encode(FORMAT))
                    conn.send("Data sent Successfully".encode(FORMAT))

                else:
                    ticket.write("Movie : James \n")
                    seat = str(seat13)
                    conn.send("Available Seats: ".encode(FORMAT))
                    conn.send(seat.encode(FORMAT))
                    conn.send("\nCost of the ticket : Rs.300/ticket\nEnter the number of seats to be booked:".encode(FORMAT))
                    
                    choice4 = int(conn.recv(SIZE).decode(FORMAT))
                    choice5 = 0
                    while((choice4 < 0 and choice4 > 100)or(choice5 < 0 and choice4 > 100)):
                        conn.send("Enter number within available number of seats:\n".encode(FORMAT))
                        choice5 = int(conn.recv(SIZE).decode(FORMAT))
                    value4 = str(300*choice4)
                    value5 = str(300*choice5)
                    if(choice4 < 0 and choice4 > 100):
                        choice5 = str(choice5)
                        ticket.write("Number of tickets booked: "+choice5+" \n")
                        ticket.write("Cost of " +choice5+ " tickets:"+ value5 +"\n")
                    else:
                        choice4 = str(choice4)
                        ticket.write("Number of tickets booked:"+ choice4+ "\n")
                        ticket.write("Cost of "+choice4+" tickets:"+ value4 +"\n")
                    # conn.send("ticket.txt".encode(FORMAT))
                    data = ticket.read()
                    print(data)
                    conn.send(data.encode(FORMAT))
                    conn.send("Data sent Successfully".encode(FORMAT))
            else:
                ticket.write("Theatre : Orien Mall \n")
                conn.send("Select the movie:\n1.Kashmir Files \n2.Radhe Shyam \n3.James".encode(FORMAT))
                choice3 = int(conn.recv(SIZE).decode(FORMAT))
                if choice3 == 1:
                    ticket.write("Movie : Kashmir Files \n")
                    seat = str(seat13)
                    conn.send("Available Seats: ".encode(FORMAT))
                    conn.send(seat.encode(FORMAT))
                    conn.send("\nCost of the ticket : Rs.300/ticket\nEnter the number of seats to be booked:".encode(FORMAT))
                    
                    choice4 = int(conn.recv(SIZE).decode(FORMAT))
                    choice5 = 0
                    while((choice4 < 0 and choice4 > 100)or(choice5 < 0 and choice4 > 100)):
                        conn.send("Enter number within available number of seats:\n".encode(FORMAT))
                        choice5 = int(conn.recv(SIZE).decode(FORMAT))
                    value4 = str(300*choice4)
                    value5 = str(300*choice5)
                    if(choice4 < 0 and choice4 > 100):
                        choice5 = str(choice5)
                        ticket.write("Number of tickets booked: "+choice5+" \n")
                        ticket.write("Cost of " +choice5+ " tickets:"+ value5 +"\n")
                    else:
                        choice4 = str(choice4)
                        ticket.write("Number of tickets booked:"+ choice4+ "\n")
                        ticket.write("Cost of "+choice4+" tickets:"+ value4 +"\n")
                    # conn.send("ticket.txt".encode(FORMAT))
                    data = ticket.read()
                    print(data)
                    conn.send(data.encode(FORMAT))
                    conn.send("Data sent Successfully".encode(FORMAT))
                elif choice3 == 2:
                    ticket.write("Movie : Radhe Shyam \n")
                    seat = str(seat13)
                    conn.send("Available Seats: ".encode(FORMAT))
                    conn.send(seat.encode(FORMAT))
                    conn.send("\nCost of the ticket : Rs.300/ticket\nEnter the number of seats to be booked:".encode(FORMAT))
                    
                    choice4 = int(conn.recv(SIZE).decode(FORMAT))
                    choice5 = 0
                    while((choice4 < 0 and choice4 > 100)or(choice5 < 0 and choice4 > 100)):
                        conn.send("Enter number within available number of seats:\n".encode(FORMAT))
                        choice5 = int(conn.recv(SIZE).decode(FORMAT))
                    value4 = str(300*choice4)
                    value5 = str(300*choice5)
                    if(choice4 < 0 and choice4 > 100):
                        choice5 = str(choice5)
                        ticket.write("Number of tickets booked: "+choice5+" \n")
                        ticket.write("Cost of " +choice5+ " tickets:"+ value5 +"\n")
                    else:
                        choice4 = str(choice4)
                        ticket.write("Number of tickets booked:"+ choice4+ "\n")
                        ticket.write("Cost of "+choice4+" tickets:"+ value4 +"\n")
                    # conn.send("ticket.txt".encode(FORMAT))
                    data = ticket.read()
                    print(data)
                    conn.send(data.encode(FORMAT))
                    conn.send("Data sent Successfully".encode(FORMAT))
                else:
                    ticket.write("Movie : James \n")
                    seat = str(seat13)
                    conn.send("Available Seats: ".encode(FORMAT))
                    conn.send(seat.encode(FORMAT))
                    conn.send("\nCost of the ticket : Rs.300/ticket\nEnter the number of seats to be booked:".encode(FORMAT))
                    
                    choice4 = int(conn.recv(SIZE).decode(FORMAT))
                    choice5 = 0
                    while((choice4 < 0 and choice4 > 100)or(choice5 < 0 and choice4 > 100)):
                        conn.send("Enter number within available number of seats:\n".encode(FORMAT))
                        choice5 = int(conn.recv(SIZE).decode(FORMAT))
                    value4 = str(300*choice4)
                    value5 = str(300*choice5)
                    if(choice4 < 0 and choice4 > 100):
                        choice5 = str(choice5)
                        ticket.write("Number of tickets booked: "+choice5+" \n")
                        ticket.write("Cost of " +choice5+ " tickets:"+ value5 +"\n")
                    else:
                        choice4 = str(choice4)
                        ticket.write("Number of tickets booked:"+ choice4+ "\n")
                        ticket.write("Cost of "+choice4+" tickets:"+ value4 +"\n")
                    # conn.send("ticket.txt".encode(FORMAT))
                    data = ticket.read()
                    print(data)
                    conn.send(data.encode(FORMAT))
                    conn.send("Data sent Successfully".encode(FORMAT))

        
        
        else:
            ticket.write("Place : Hosekerahalli \n")
            conn.send("Select the theatre:\n1.Gopalan Mall \n2.Orien Mall".encode(FORMAT))
            choice2 = int(conn.recv(SIZE).decode(FORMAT))
            if choice2 == 1:
                ticket.write("Theatre : Gopalan Mall \n")
                conn.send("Select the movie:\n1.Kashmir Files \n2.Radhe Shyam \n3.James".encode(FORMAT))
                choice3 = int(conn.recv(SIZE).decode(FORMAT))
                if choice3 == 1:
                    ticket.write("Movie : Kashmir Files \n")
                    seat = str(seat13)
                    conn.send("Available Seats: ".encode(FORMAT))
                    conn.send(seat.encode(FORMAT))
                    conn.send("\nCost of the ticket : Rs.300/ticket\nEnter the number of seats to be booked:".encode(FORMAT))
                    
                    choice4 = int(conn.recv(SIZE).decode(FORMAT))
                    choice5 = 0
                    while((choice4 < 0 and choice4 > 100)or(choice5 < 0 and choice4 > 100)):
                        conn.send("Enter number within available number of seats:\n".encode(FORMAT))
                        choice5 = int(conn.recv(SIZE).decode(FORMAT))
                    value4 = str(300*choice4)
                    value5 = str(300*choice5)
                    if(choice4 < 0 and choice4 > 100):
                        choice5 = str(choice5)
                        ticket.write("Number of tickets booked: "+choice5+" \n")
                        ticket.write("Cost of " +choice5+ " tickets:"+ value5 +"\n")
                    else:
                        choice4 = str(choice4)
                        ticket.write("Number of tickets booked:"+ choice4+ "\n")
                        ticket.write("Cost of "+choice4+" tickets:"+ value4 +"\n")
                    # conn.send("ticket.txt".encode(FORMAT))
                    data = ticket.read()
                    print(data)
                    conn.send(data.encode(FORMAT))
                    conn.send("Data sent Successfully".encode(FORMAT))

                elif choice3 == 2:
                    ticket.write("Movie : Radhe Shyam \n")
                    seat = str(seat13)
                    conn.send("Available Seats: ".encode(FORMAT))
                    conn.send(seat.encode(FORMAT))
                    conn.send("\nCost of the ticket : Rs.300/ticket\nEnter the number of seats to be booked:".encode(FORMAT))
                    
                    choice4 = int(conn.recv(SIZE).decode(FORMAT))
                    choice5 = 0
                    while((choice4 < 0 and choice4 > 100)or(choice5 < 0 and choice4 > 100)):
                        conn.send("Enter number within available number of seats:\n".encode(FORMAT))
                        choice5 = int(conn.recv(SIZE).decode(FORMAT))
                    value4 = str(300*choice4)
                    value5 = str(300*choice5)
                    if(choice4 < 0 and choice4 > 100):
                        choice5 = str(choice5)
                        ticket.write("Number of tickets booked: "+choice5+" \n")
                        ticket.write("Cost of " +choice5+ " tickets:"+ value5 +"\n")
                    else:
                        choice4 = str(choice4)
                        ticket.write("Number of tickets booked:"+ choice4+ "\n")
                        ticket.write("Cost of "+choice4+" tickets:"+ value4 +"\n")
                    # conn.send("ticket.txt".encode(FORMAT))
                    data = ticket.read()
                    print(data)
                    conn.send(data.encode(FORMAT))
                    conn.send("Data sent Successfully".encode(FORMAT))

                else:
                    ticket.write("Movie : James \n")
                    seat = str(seat13)
                    conn.send("Available Seats: ".encode(FORMAT))
                    conn.send(seat.encode(FORMAT))
                    conn.send("\nCost of the ticket : Rs.300/ticket\nEnter the number of seats to be booked:".encode(FORMAT))
                    
                    choice4 = int(conn.recv(SIZE).decode(FORMAT))
                    choice5 = 0
                    while((choice4 < 0 and choice4 > 100)or(choice5 < 0 and choice4 > 100)):
                        conn.send("Enter number within available number of seats:\n".encode(FORMAT))
                        choice5 = int(conn.recv(SIZE).decode(FORMAT))
                    value4 = str(300*choice4)
                    value5 = str(300*choice5)
                    if(choice4 < 0 and choice4 > 100):
                        choice5 = str(choice5)
                        ticket.write("Number of tickets booked: "+choice5+" \n")
                        ticket.write("Cost of " +choice5+ " tickets:"+ value5 +"\n")
                    else:
                        choice4 = str(choice4)
                        ticket.write("Number of tickets booked:"+ choice4+ "\n")
                        ticket.write("Cost of "+choice4+" tickets:"+ value4 +"\n")
                    # conn.send("ticket.txt".encode(FORMAT))
                    data = ticket.read()
                    print(data)
                    conn.send(data.encode(FORMAT))
                    conn.send("Data sent Successfully".encode(FORMAT))

            else:
                ticket.write("Theatre : Orien Mall \n")
                conn.send("Select the movie:\n1.Kashmir Files \n2.Radhe Shyam \n3.James".encode(FORMAT))
                choice3 = int(conn.recv(SIZE).decode(FORMAT))
                if choice3 == 1:
                    ticket.write("Movie : Kashmir Files \n")
                    seat = str(seat13)
                    conn.send("Available Seats: ".encode(FORMAT))
                    conn.send(seat.encode(FORMAT))
                    conn.send("\nCost of the ticket : Rs.300/ticket\nEnter the number of seats to be booked:".encode(FORMAT))
                    
                    choice4 = int(conn.recv(SIZE).decode(FORMAT))
                    choice5 = 0
                    while((choice4 < 0 and choice4 > 100)or(choice5 < 0 and choice4 > 100)):
                        conn.send("Enter number within available number of seats:\n".encode(FORMAT))
                        choice5 = int(conn.recv(SIZE).decode(FORMAT))
                    value4 = str(300*choice4)
                    value5 = str(300*choice5)
                    if(choice4 < 0 and choice4 > 100):
                        choice5 = str(choice5)
                        ticket.write("Number of tickets booked: "+choice5+" \n")
                        ticket.write("Cost of " +choice5+ " tickets:"+ value5 +"\n")
                    else:
                        choice4 = str(choice4)
                        ticket.write("Number of tickets booked:"+ choice4+ "\n")
                        ticket.write("Cost of "+choice4+" tickets:"+ value4 +"\n")
                    # conn.send("ticket.txt".encode(FORMAT))
                    data = ticket.read()
                    print(data)
                    conn.send(data.encode(FORMAT))
                    conn.send("Data sent Successfully".encode(FORMAT))
                
                elif choice3 == 2:
                    ticket.write("Movie : Radhe Shyam \n")
                    seat = str(seat13)
                    conn.send("Available Seats: ".encode(FORMAT))
                    conn.send(seat.encode(FORMAT))
                    conn.send("\nCost of the ticket : Rs.300/ticket\nEnter the number of seats to be booked:".encode(FORMAT))
                    
                    choice4 = int(conn.recv(SIZE).decode(FORMAT))
                    choice5 = 0
                    while((choice4 < 0 and choice4 > 100)or(choice5 < 0 and choice4 > 100)):
                        conn.send("Enter number within available number of seats:\n".encode(FORMAT))
                        choice5 = int(conn.recv(SIZE).decode(FORMAT))
                    value4 = str(300*choice4)
                    value5 = str(300*choice5)
                    if(choice4 < 0 and choice4 > 100):
                        choice5 = str(choice5)
                        ticket.write("Number of tickets booked: "+choice5+" \n")
                        ticket.write("Cost of " +choice5+ " tickets:"+ value5 +"\n")
                    else:
                        choice4 = str(choice4)
                        ticket.write("Number of tickets booked:"+ choice4+ "\n")
                        ticket.write("Cost of "+choice4+" tickets:"+ value4 +"\n")
                    # conn.send("ticket.txt".encode(FORMAT))
                    data = ticket.read()
                    print(data)
                    conn.send(data.encode(FORMAT))
                    conn.send("Data sent Successfully".encode(FORMAT))

                else:
                    ticket.write("Movie : James \n")
                    seat = str(seat13)
                    conn.send("Available Seats: ".encode(FORMAT))
                    conn.send(seat.encode(FORMAT))
                    conn.send("\nCost of the ticket : Rs.300/ticket\nEnter the number of seats to be booked:".encode(FORMAT))
                    
                    choice4 = int(conn.recv(SIZE).decode(FORMAT))
                    choice5 = 0
                    while((choice4 < 0 and choice4 > 100)or(choice5 < 0 and choice4 > 100)):
                        conn.send("Enter number within available number of seats:\n".encode(FORMAT))
                        choice5 = int(conn.recv(SIZE).decode(FORMAT))
                    value4 = str(300*choice4)
                    value5 = str(300*choice5)
                    if(choice4 < 0 and choice4 > 100):
                        choice5 = str(choice5)
                        ticket.write("Number of tickets booked: "+choice5+" \n")
                        ticket.write("Cost of " +choice5+ " tickets:"+ value5 +"\n")
                    else:
                        choice4 = str(choice4)
                        ticket.write("Number of tickets booked:"+ choice4+ "\n")
                        ticket.write("Cost of "+choice4+" tickets:"+ value4 +"\n")
                    # conn.send("ticket.txt".encode(FORMAT))
                    data = ticket.read()
                    print(data)
                    conn.send(data.encode(FORMAT))
                    conn.send("Data sent Successfully".encode(FORMAT))

        
        
            
        # print(data)
       

        # print("[RECV] Filename received")
        # file = open("serverdata/"+filename, "w")
        # conn.send("Filename received".encode(FORMAT))

        # data = conn.recv(SIZE).decode(FORMAT)
        # print(f"[RECV] File data received")
        # file.write(data)
        # conn.send("File data received".encode(FORMAT))

        ticket.close()
        conn.close()
        print(f"[DISCONNECTED] {addr} disconnected.")

              
       
    


if __name__ == "__main__":
    main()