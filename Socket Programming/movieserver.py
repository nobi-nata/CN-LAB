import socket
from _thread import *
IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP,PORT)
FORMAT = "utf-8"
SIZE = 1024
PLACES = ['Banashankari','Hoskerahalli']
THETARE = ['Gopalan','Oriean']
MOVIE = ['Kashmir Files','Radhe Shyam','James']
ThreadCount = 0

seat111 = 100
seat112 = 100
seat113 = 100
seat121 = 100
seat122 = 100
seat123 = 100
seat211 = 100
seat212 = 100
seat213 = 100
seat221 = 100
seat222 = 100
seat223 = 100
print("[STARTING] Server is starting.")
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)
server.listen(5)
print("[LISTENING] Server is listening.")




def threaded_client(connection):
    
    # a = 1
    
    # connection,addr = server.accept()
    # print(f"[NEW CONNECTION] {addr} connected.")
    # str1 = str(a)
    # filename = "ticket" + str1 + ".txt"
    # a = a + 1
    # ticket = open("serverdata/"+filename,'w+')
    
    # ticket.write("-----------MOVIE TICKET------------\n")
    heading = "-----------MOVIE TICKET------------"
    connection.send("-------------------LHN MOVIE BOOKING SYSTEM--------------------\n".encode(FORMAT))
    connection.send("Enter Your Name : ".encode(FORMAT))
    name = connection.recv(SIZE).decode(FORMAT)
    # ticket.write("Name : "+name+ "\n")
    name1 = "Name : " + name
    connection.send("Select the place:\n1.Banashankari \n2.Hosekerahalli".encode(FORMAT))
    choice1 = int(connection.recv(SIZE).decode(FORMAT))
    if choice1 == 1:
        # ticket.write("Place : Banashankari \n")
        place = "\nPlace : Banashankari "
        connection.send("Select the theatre:\n1.Gopalan Mall \n2.Orien Mall".encode(FORMAT))
        choice2 = int(connection.recv(SIZE).decode(FORMAT))
        if choice2 == 1:
            # ticket.write("Theatre : Gopalan Mall \n")
            theatre = "\nTheatre : Gopalan Mall "
            connection.send("Select the movie:\n1.Kashmir Files \n2.Radhe Shyam \n3.James".encode(FORMAT))
            choice3 = int(connection.recv(SIZE).decode(FORMAT))
            if choice3 == 1:
                seat = str(seat111)
                connection.send("Available Seats: ".encode(FORMAT))
                connection.send(seat.encode(FORMAT))
                # ticket.write("Movie : Kashmir Files \n")
                movie = "\nMovie : Kashmir Files"
                connection.send("\nCost of the ticket : Rs.300/ticket\nEnter the number of seats to be booked:".encode(FORMAT))
                choice4 = int(connection.recv(SIZE).decode(FORMAT))
                choice5 = -1
                while((choice4 < 0 or choice4 > 100)and(choice5 < 0 or choice5 > 100)):
                    connection.send("Enter number within available number of seats:".encode(FORMAT))
                    choice5 = int(connection.recv(SIZE).decode(FORMAT))
                value4 = str(300*choice4)
                value5 = str(300*choice5)
                if(choice4 < 0 or choice4 > 100):
                    choice5 = str(choice5)
                    # ticket.write("Number of tickets booked: "+choice5+" \n")
                    nooftickets = "\nNumber of tickets booked: "+choice5
                    # ticket.write("Cost of " +choice5+ " tickets: Rs. "+ value5 +"\n")
                    cost = "\nCost of " +choice5+ " tickets: Rs. "+ value5 
                else:
                    choice4 = str(choice4)
                    # ticket.write("Number of tickets booked:"+ choice4+ "\n")
                    # ticket.write("Cost of "+choice4+" tickets: Rs. "+ value4 +"\n")
                    nooftickets = "\nNumber of tickets booked: "+choice4
                    cost = "\nCost of " + choice4 + " tickets: Rs. "+ value4
                # connection.send("ticket.txt".encode(FORMAT))
                # data = ticket.read()
                # print(data)
                # connection.send(("ticket"+str1+".txt").encode(FORMAT))
                # connection.send(data.encode(FORMAT))
                connection.send("Would you like to confirm booking?['yes' or 'no']".encode(FORMAT))
                choice6 = connection.recv(SIZE).decode(FORMAT)
                if(choice6 == 'yes'):
                    connection.send(heading.encode(FORMAT))
                    connection.send(name1.encode(FORMAT))
                    connection.send(place.encode(FORMAT))
                    connection.send(theatre.encode(FORMAT))
                    connection.send(movie.encode(FORMAT))
                    connection.send(nooftickets.encode(FORMAT))
                    connection.send(cost.encode(FORMAT))
                    connection.send("\nTicket Booked Successfully\nThank You for visiting LHN Movie Booking".encode(FORMAT))
                else:
                    connection.send("\nThank You for visiting LHN Movie Booking".encode(FORMAT))
            elif choice3 == 2:
                # ticket.write("Movie : Radhe Shyam \n")
                movie = "\nMovie : Radhe Shyam"
                seat = str(seat112)
                connection.send("Available Seats: ".encode(FORMAT))
                connection.send(seat.encode(FORMAT))
                connection.send("\nCost of the ticket : Rs.300/ticket\nEnter the number of seats to be booked:".encode(FORMAT))
                
                choice4 = int(connection.recv(SIZE).decode(FORMAT))
                choice5 = -1
                while((choice4 < 0 or choice4 > 100)and(choice5 < 0 or choice5 > 100)):
                    connection.send("Enter number within available number of seats:".encode(FORMAT))
                    choice5 = int(connection.recv(SIZE).decode(FORMAT))
                value4 = str(300*choice4)
                value5 = str(300*choice5)
                if(choice4 < 0 or choice4 > 100):
                    choice5 = str(choice5)
                    # ticket.write("Number of tickets booked: "+choice5+" \n")
                    nooftickets = "\nNumber of tickets booked: "+choice5
                    # ticket.write("Cost of " +choice5+ " tickets: Rs. "+ value5 +"\n")
                    cost = "\nCost of " +choice5+ " tickets: Rs. "+ value5
                else:
                    choice4 = str(choice4)
                    # ticket.write("Number of tickets booked:"+ choice4+ "\n")
                    # ticket.write("Cost of "+choice4+" tickets: Rs. "+ value4 +"\n")
                    nooftickets = "\nNumber of tickets booked: "+choice4
                    cost = "\nCost of " + choice4 + " tickets: Rs. "+ value4
                # connection.send("ticket.txt".encode(FORMAT))
                # data = ticket.read()
                # print(data)
                # connection.send(data.encode(FORMAT))
                # connection.send("Data sent Successfully".encode(FORMAT))
                connection.send("Would you like to confirm booking?['yes' or 'no']".encode(FORMAT))
                choice6 = connection.recv(SIZE).decode(FORMAT)
                if(choice6 == 'yes'):
                    connection.send(heading.encode(FORMAT))
                    connection.send(name1.encode(FORMAT))
                    connection.send(place.encode(FORMAT))
                    connection.send(theatre.encode(FORMAT))
                    connection.send(movie.encode(FORMAT))
                    connection.send(nooftickets.encode(FORMAT))
                    connection.send(cost.encode(FORMAT))
                    connection.send("\nTicket Booked Successfully\nThank You for visiting LHN Movie Booking".encode(FORMAT))
                else:
                    connection.send("\nThank You for visiting LHN Movie Booking".encode(FORMAT))
            
            else:
                # ticket.write("Movie : James \n")
                movie = "\nMovie : James"
                seat = str(seat113)
                connection.send("Available Seats: ".encode(FORMAT))
                connection.send(seat.encode(FORMAT))
                connection.send("\nCost of the ticket : Rs.300/ticket\nEnter the number of seats to be booked:".encode(FORMAT))
                
                choice4 = int(connection.recv(SIZE).decode(FORMAT))
                choice5 = -1
                while((choice4 < 0 or choice4 > 100)and(choice5 < 0 or choice5 > 100)):
                    connection.send("Enter number within available number of seats:".encode(FORMAT))
                    choice5 = int(connection.recv(SIZE).decode(FORMAT))
                value4 = str(300*choice4)
                value5 = str(300*choice5)
                if(choice4 < 0 or choice4 > 100):
                    choice5 = str(choice5)
                    # ticket.write("Number of tickets booked: "+choice5+" \n")
                    nooftickets = "\nNumber of tickets booked: "+choice5
                    # ticket.write("Cost of " +choice5+ " tickets: Rs. "+ value5 +"\n")
                    cost = "\nCost of " +choice5+ " tickets: Rs. "+ value5
                else:
                    choice4 = str(choice4)
                    # ticket.write("Number of tickets booked:"+ choice4+ "\n")
                    # ticket.write("Cost of "+choice4+" tickets: Rs. "+ value4 +"\n")
                    nooftickets = "\nNumber of tickets booked: "+choice4
                    cost = "\nCost of " + choice4 + " tickets: Rs. "+ value4
                # connection.send("ticket.txt".encode(FORMAT))
                # data = ticket.read()
                # print(data)
                # connection.send(data.encode(FORMAT))
                # connection.send("Data sent Successfully".encode(FORMAT))
                connection.send("Would you like to confirm booking?['yes' or 'no']".encode(FORMAT))
                choice6 = connection.recv(SIZE).decode(FORMAT)
                if(choice6 == 'yes'):
                    connection.send(heading.encode(FORMAT))
                    connection.send(name1.encode(FORMAT))
                    connection.send(place.encode(FORMAT))
                    connection.send(theatre.encode(FORMAT))
                    connection.send(movie.encode(FORMAT))
                    connection.send(nooftickets.encode(FORMAT))
                    connection.send(cost.encode(FORMAT))
                    connection.send("\nTicket Booked Successfully\nThank You for visiting LHN Movie Booking".encode(FORMAT))
                else:
                    connection.send("\nThank You for visiting LHN Movie Booking".encode(FORMAT))
        else:
            # ticket.write("Theatre : Orien Mall \n")
            theatre = "\nTheatre : Orien Mall"
            connection.send("Select the movie:\n1.Kashmir Files \n2.Radhe Shyam \n3.James".encode(FORMAT))
            choice3 = int(connection.recv(SIZE).decode(FORMAT))
            if choice3 == 1:
                # ticket.write("Movie : Kashmir Files \n")
                movie = "\nMovie : Kashmir Files"
                seat = str(seat121)
                connection.send("Available Seats: ".encode(FORMAT))
                connection.send(seat.encode(FORMAT))
                connection.send("\nCost of the ticket : Rs.300/ticket\nEnter the number of seats to be booked:".encode(FORMAT))
                
                choice4 = int(connection.recv(SIZE).decode(FORMAT))
                choice5 = -1
                while((choice4 < 0 or choice4 > 100)and(choice5 < 0 or choice5 > 100)):
                    connection.send("Enter number within available number of seats:".encode(FORMAT))
                    choice5 = int(connection.recv(SIZE).decode(FORMAT))
                value4 = str(300*choice4)
                value5 = str(300*choice5)
                if(choice4 < 0 or choice4 > 100):
                    choice5 = str(choice5)
                    # ticket.write("Number of tickets booked: "+choice5+" \n")
                    nooftickets = "\nNumber of tickets booked: "+choice5
                    # ticket.write("Cost of " +choice5+ " tickets: Rs. "+ value5 +"\n")
                    cost = "\nCost of " +choice5+ " tickets: Rs. "+ value5
                else:
                    choice4 = str(choice4)
                    # ticket.write("Number of tickets booked:"+ choice4+ "\n")
                    # ticket.write("Cost of "+choice4+" tickets: Rs. "+ value4 +"\n")
                    nooftickets = "\nNumber of tickets booked: "+choice4
                    cost = "\nCost of " + choice4 + " tickets: Rs. "+ value4
                # connection.send("ticket.txt".encode(FORMAT))
                # data = ticket.read()
                # print(data)
                # connection.send(data.encode(FORMAT))
                # connection.send("Data sent Successfully".encode(FORMAT))
                connection.send("Would you like to confirm booking?['yes' or 'no']".encode(FORMAT))
                choice6 = connection.recv(SIZE).decode(FORMAT)
                if(choice6 == 'yes'):
                    connection.send(heading.encode(FORMAT))
                    connection.send(name1.encode(FORMAT))
                    connection.send(place.encode(FORMAT))
                    connection.send(theatre.encode(FORMAT))
                    connection.send(movie.encode(FORMAT))
                    connection.send(nooftickets.encode(FORMAT))
                    connection.send(cost.encode(FORMAT))
                    connection.send("\nTicket Booked Successfully\nThank You for visiting LHN Movie Booking".encode(FORMAT))
                else:
                    connection.send("\nThank You for visiting LHN Movie Booking".encode(FORMAT))
            elif choice3 == 2:
                # ticket.write("Movie : Radhe Shyam \n")
                movie = "\nMovie : Radhe Shyam"
                seat = str(seat122)
                connection.send("Available Seats: ".encode(FORMAT))
                connection.send(seat.encode(FORMAT))
                connection.send("\nCost of the ticket : Rs.300/ticket\nEnter the number of seats to be booked:".encode(FORMAT))
                
                choice4 = int(connection.recv(SIZE).decode(FORMAT))
                choice5 = -1
                while((choice4 < 0 or choice4 > 100)and(choice5 < 0 or choice5 > 100)):
                    connection.send("Enter number within available number of seats:".encode(FORMAT))
                    choice5 = int(connection.recv(SIZE).decode(FORMAT))
                value4 = str(300*choice4)
                value5 = str(300*choice5)
                if(choice4 < 0 or choice4 > 100):
                    choice5 = str(choice5)
                    # ticket.write("Number of tickets booked: "+choice5+" \n")
                    nooftickets = "\nNumber of tickets booked: "+choice5
                    # ticket.write("Cost of " +choice5+ " tickets: Rs. "+ value5 +"\n")
                    cost = "\nCost of " +choice5+ " tickets: Rs. "+ value5
                else:
                    choice4 = str(choice4)
                    # ticket.write("Number of tickets booked:"+ choice4+ "\n")
                    # ticket.write("Cost of "+choice4+" tickets: Rs. "+ value4 +"\n")
                    nooftickets = "\nNumber of tickets booked: "+choice4
                    cost = "\nCost of " + choice4 + " tickets: Rs. "+ value4
                # connection.send("ticket.txt".encode(FORMAT))
                # data = ticket.read()
                # print(data)
                # connection.send(data.encode(FORMAT))
                # connection.send("Data sent Successfully".encode(FORMAT))
                connection.send("Would you like to confirm booking?['yes' or 'no']".encode(FORMAT))
                choice6 = connection.recv(SIZE).decode(FORMAT)
                if(choice6 == 'yes'):
                    connection.send(heading.encode(FORMAT))
                    connection.send(name1.encode(FORMAT))
                    connection.send(place.encode(FORMAT))
                    connection.send(theatre.encode(FORMAT))
                    connection.send(movie.encode(FORMAT))
                    connection.send(nooftickets.encode(FORMAT))
                    connection.send(cost.encode(FORMAT))
                    connection.send("\nTicket Booked Successfully\nThank You for visiting LHN Movie Booking".encode(FORMAT))
                else:
                    connection.send("\nThank You for visiting LHN Movie Booking".encode(FORMAT))
            else:
                # ticket.write("Movie : James \n")
                movie = "\nMovie : James"
                seat = str(seat123)
                connection.send("Available Seats: ".encode(FORMAT))
                connection.send(seat.encode(FORMAT))
                connection.send("\nCost of the ticket : Rs.300/ticket\nEnter the number of seats to be booked:".encode(FORMAT))
                
                choice4 = int(connection.recv(SIZE).decode(FORMAT))
                choice5 = -1
                while((choice4 < 0 or choice4 > 100)and(choice5 < 0 or choice5 > 100)):
                    connection.send("Enter number within available number of seats:".encode(FORMAT))
                    choice5 = int(connection.recv(SIZE).decode(FORMAT))
                value4 = str(300*choice4)
                value5 = str(300*choice5)
                if(choice4 < 0 or choice4 > 100):
                    choice5 = str(choice5)
                    # ticket.write("Number of tickets booked: "+choice5+" \n")
                    nooftickets = "\nNumber of tickets booked: "+choice5
                    # ticket.write("Cost of " +choice5+ " tickets: Rs. "+ value5 +"\n")
                    cost = "\nCost of " +choice5+ " tickets: Rs. "+ value5
                else:
                    choice4 = str(choice4)
                    # ticket.write("Number of tickets booked:"+ choice4+ "\n")
                    # ticket.write("Cost of "+choice4+" tickets: Rs. "+ value4 +"\n")
                    nooftickets = "\nNumber of tickets booked: "+choice4
                    cost = "\nCost of " + choice4 + " tickets: Rs. "+ value4
                # connection.send("ticket.txt".encode(FORMAT))
                # data = ticket.read()
                # print(data)
                # connection.send(data.encode(FORMAT))
                # connection.send("Data sent Successfully".encode(FORMAT))
                connection.send("Would you like to confirm booking?['yes' or 'no']".encode(FORMAT))
                choice6 = connection.recv(SIZE).decode(FORMAT)
                if(choice6 == 'yes'):
                    connection.send(heading.encode(FORMAT))
                    connection.send(name1.encode(FORMAT))
                    connection.send(place.encode(FORMAT))
                    connection.send(theatre.encode(FORMAT))
                    connection.send(movie.encode(FORMAT))
                    connection.send(nooftickets.encode(FORMAT))
                    connection.send(cost.encode(FORMAT))
                    connection.send("\nTicket Booked Successfully\nThank You for visiting LHN Movie Booking".encode(FORMAT))
                else:
                    connection.send("\nThank You for visiting LHN Movie Booking".encode(FORMAT))
    
    
    else:
        # ticket.write("Place : Hosekerahalli \n")
        place = "\nPlace : Hosekerahalli "
        connection.send("Select the theatre:\n1.Gopalan Mall \n2.Orien Mall".encode(FORMAT))
        choice2 = int(connection.recv(SIZE).decode(FORMAT))
        if choice2 == 1:
            # ticket.write("Theatre : Gopalan Mall \n")
            theatre = "\nTheatre : Gopalan Mall "
            connection.send("Select the movie:\n1.Kashmir Files \n2.Radhe Shyam \n3.James".encode(FORMAT))
            choice3 = int(connection.recv(SIZE).decode(FORMAT))
            if choice3 == 1:
                # ticket.write("Movie : Kashmir Files \n")
                movie = "\nMovie : Kashmir Files"
                seat = str(seat211)
                connection.send("Available Seats: ".encode(FORMAT))
                connection.send(seat.encode(FORMAT))
                connection.send("\nCost of the ticket : Rs.300/ticket\nEnter the number of seats to be booked:".encode(FORMAT))
                
                choice4 = int(connection.recv(SIZE).decode(FORMAT))
                choice5 = -1
                while((choice4 < 0 or choice4 > 100)and(choice5 < 0 or choice5 > 100)):
                    connection.send("Enter number within available number of seats:".encode(FORMAT))
                    choice5 = int(connection.recv(SIZE).decode(FORMAT))
                value4 = str(300*choice4)
                value5 = str(300*choice5)
                if(choice4 < 0 or choice4 > 100):
                    choice5 = str(choice5)
                    # ticket.write("Number of tickets booked: "+choice5+" \n")
                    nooftickets = "\nNumber of tickets booked: "+choice5
                    # ticket.write("Cost of " +choice5+ " tickets: Rs. "+ value5 +"\n")
                    cost = "\nCost of " +choice5+ " tickets: Rs. "+ value5
                else:
                    choice4 = str(choice4)
                    # ticket.write("Number of tickets booked:"+ choice4+ "\n")
                    # ticket.write("Cost of "+choice4+" tickets: Rs. "+ value4 +"\n")
                    nooftickets = "\nNumber of tickets booked: "+choice4
                    cost = "\nCost of " + choice4 + " tickets: Rs. "+ value4
                # connection.send("ticket.txt".encode(FORMAT))
                # data = ticket.read()
                # print(data)
                # connection.send(data.encode(FORMAT))
                # connection.send("Data sent Successfully".encode(FORMAT))
                connection.send("Would you like to confirm booking?['yes' or 'no']".encode(FORMAT))
                choice6 = connection.recv(SIZE).decode(FORMAT)
                if(choice6 == 'yes'):
                    connection.send(heading.encode(FORMAT))
                    connection.send(name1.encode(FORMAT))
                    connection.send(place.encode(FORMAT))
                    connection.send(theatre.encode(FORMAT))
                    connection.send(movie.encode(FORMAT))
                    connection.send(nooftickets.encode(FORMAT))
                    connection.send(cost.encode(FORMAT))
                    connection.send("\nTicket Booked Successfully\nThank You for visiting LHN Movie Booking".encode(FORMAT))
                else:
                    connection.send("\nThank You for visiting LHN Movie Booking".encode(FORMAT))
            
            elif choice3 == 2:
                # ticket.write("Movie : Radhe Shyam \n")
                movie = "\nMovie : Radhe Shyam"
                seat = str(seat212)
                connection.send("Available Seats: ".encode(FORMAT))
                connection.send(seat.encode(FORMAT))
                connection.send("\nCost of the ticket : Rs.300/ticket\nEnter the number of seats to be booked:".encode(FORMAT))
                
                choice4 = int(connection.recv(SIZE).decode(FORMAT))
                choice5 = -1
                while((choice4 < 0 or choice4 > 100)and(choice5 < 0 or choice5 > 100)):
                    connection.send("Enter number within available number of seats:".encode(FORMAT))
                    choice5 = int(connection.recv(SIZE).decode(FORMAT))
                value4 = str(300*choice4)
                value5 = str(300*choice5)
                if(choice4 < 0 or choice4 > 100):
                    choice5 = str(choice5)
                    # ticket.write("Number of tickets booked: "+choice5+" \n")
                    nooftickets = "\nNumber of tickets booked: "+choice5
                    # ticket.write("Cost of " +choice5+ " tickets: Rs. "+ value5 +"\n")
                    cost = "\nCost of " +choice5+ " tickets: Rs. "+ value5
                else:
                    choice4 = str(choice4)
                    # ticket.write("Number of tickets booked:"+ choice4+ "\n")
                    # ticket.write("Cost of "+choice4+" tickets: Rs. "+ value4 +"\n")
                    nooftickets = "\nNumber of tickets booked: "+choice4
                    cost = "\nCost of " + choice4 + " tickets: Rs. "+ value4
                # connection.send("ticket.txt".encode(FORMAT))
                # data = ticket.read()
                # print(data)
                # connection.send(data.encode(FORMAT))
                # connection.send("Data sent Successfully".encode(FORMAT))
                connection.send("Would you like to confirm booking?['yes' or 'no']".encode(FORMAT))
                choice6 = connection.recv(SIZE).decode(FORMAT)
                if(choice6 == 'yes'):
                    connection.send(heading.encode(FORMAT))
                    connection.send(name1.encode(FORMAT))
                    connection.send(place.encode(FORMAT))
                    connection.send(theatre.encode(FORMAT))
                    connection.send(movie.encode(FORMAT))
                    connection.send(nooftickets.encode(FORMAT))
                    connection.send(cost.encode(FORMAT))
                    connection.send("\nTicket Booked Successfully\nThank You for visiting LHN Movie Booking".encode(FORMAT))
                else:
                    connection.send("\nThank You for visiting LHN Movie Booking".encode(FORMAT))
            
            else:
                # ticket.write("Movie : James \n")
                movie = "\nMovie : James"
                seat = str(seat213)
                connection.send("Available Seats: ".encode(FORMAT))
                connection.send(seat.encode(FORMAT))
                connection.send("\nCost of the ticket : Rs.300/ticket\nEnter the number of seats to be booked:".encode(FORMAT))
                
                choice4 = int(connection.recv(SIZE).decode(FORMAT))
                choice5 = -1
                while((choice4 < 0 or choice4 > 100)and(choice5 < 0 or choice5 > 100)):
                    connection.send("Enter number within available number of seats:".encode(FORMAT))
                    choice5 = int(connection.recv(SIZE).decode(FORMAT))
                value4 = str(300*choice4)
                value5 = str(300*choice5)
                if(choice4 < 0 or choice4 > 100):
                    choice5 = str(choice5)
                    # ticket.write("Number of tickets booked: "+choice5+" \n")
                    nooftickets = "\nNumber of tickets booked: "+choice5
                    # ticket.write("Cost of " +choice5+ " tickets: Rs. "+ value5 +"\n")
                    cost = "\nCost of " +choice5+ " tickets: Rs. "+ value5
                else:
                    choice4 = str(choice4)
                    # ticket.write("Number of tickets booked:"+ choice4+ "\n")
                    # ticket.write("Cost of "+choice4+" tickets: Rs. "+ value4 +"\n")
                    nooftickets = "\nNumber of tickets booked: "+choice4
                    cost = "\nCost of " + choice4 + " tickets: Rs. "+ value4
                # connection.send("ticket.txt".encode(FORMAT))
                # data = ticket.read()
                # print(data)
                # connection.send(data.encode(FORMAT))
                # connection.send("Data sent Successfully".encode(FORMAT))
                connection.send("Would you like to confirm booking?['yes' or 'no']".encode(FORMAT))
                choice6 = connection.recv(SIZE).decode(FORMAT)
                if(choice6 == 'yes'):
                    connection.send(heading.encode(FORMAT))
                    connection.send(name1.encode(FORMAT))
                    connection.send(place.encode(FORMAT))
                    connection.send(theatre.encode(FORMAT))
                    connection.send(movie.encode(FORMAT))
                    connection.send(nooftickets.encode(FORMAT))
                    connection.send(cost.encode(FORMAT))
                    connection.send("\nTicket Booked Successfully\nThank You for visiting LHN Movie Booking".encode(FORMAT))
                else:
                    connection.send("\nThank You for visiting LHN Movie Booking".encode(FORMAT))
            
        else:
            # ticket.write("Theatre : Orien Mall \n")
            theatre = "\nTheatre : Orien Mall"
            connection.send("Select the movie:\n1.Kashmir Files \n2.Radhe Shyam \n3.James".encode(FORMAT))
            choice3 = int(connection.recv(SIZE).decode(FORMAT))
            if choice3 == 1:
                # ticket.write("Movie : Kashmir Files \n")
                movie = "\nMovie : Kashmir Files"
                seat = str(seat221)
                connection.send("Available Seats: ".encode(FORMAT))
                connection.send(seat.encode(FORMAT))
                connection.send("\nCost of the ticket : Rs.300/ticket\nEnter the number of seats to be booked:".encode(FORMAT))
                
                choice4 = int(connection.recv(SIZE).decode(FORMAT))
                choice5 = -1
                while((choice4 < 0 or choice4 > 100)and(choice5 < 0 or choice5 > 100)):
                    connection.send("Enter number within available number of seats:".encode(FORMAT))
                    choice5 = int(connection.recv(SIZE).decode(FORMAT))
                value4 = str(300*choice4)
                value5 = str(300*choice5)
                if(choice4 < 0 or choice4 > 100):
                    choice5 = str(choice5)
                    # ticket.write("Number of tickets booked: "+choice5+" \n")
                    nooftickets = "\nNumber of tickets booked: "+choice5
                    # ticket.write("Cost of " +choice5+ " tickets: Rs. "+ value5 +"\n")
                    cost = "\nCost of " +choice5+ " tickets: Rs. "+ value5
                else:
                    choice4 = str(choice4)
                    # ticket.write("Number of tickets booked:"+ choice4+ "\n")
                    # ticket.write("Cost of "+choice4+" tickets: Rs. "+ value4 +"\n")
                    nooftickets = "\nNumber of tickets booked: "+choice4
                    cost = "\nCost of " + choice4 + " tickets: Rs. "+ value4
                # connection.send("ticket.txt".encode(FORMAT))
                # data = ticket.read()
                # print(data)
                # connection.send(data.encode(FORMAT))
                # connection.send("Data sent Successfully".encode(FORMAT))
                connection.send("Would you like to confirm booking?['yes' or 'no']".encode(FORMAT))
                choice6 = connection.recv(SIZE).decode(FORMAT)
                if(choice6 == 'yes'):
                    connection.send(heading.encode(FORMAT))
                    connection.send(name1.encode(FORMAT))
                    connection.send(place.encode(FORMAT))
                    connection.send(theatre.encode(FORMAT))
                    connection.send(movie.encode(FORMAT))
                    connection.send(nooftickets.encode(FORMAT))
                    connection.send(cost.encode(FORMAT))
                    connection.send("\nTicket Booked Successfully\nThank You for visiting LHN Movie Booking".encode(FORMAT))
                else:
                    connection.send("\nThank You for visiting LHN Movie Booking".encode(FORMAT))
                            
            elif choice3 == 2:
                # ticket.write("Movie : Radhe Shyam \n")
                movie = "\nMovie : Radhe Shyam"
                seat = str(seat222)
                connection.send("Available Seats: ".encode(FORMAT))
                connection.send(seat.encode(FORMAT))
                connection.send("\nCost of the ticket : Rs.300/ticket\nEnter the number of seats to be booked:".encode(FORMAT))
                
                choice4 = int(connection.recv(SIZE).decode(FORMAT))
                choice5 = -1
                while((choice4 < 0 or choice4 > 100)and(choice5 < 0 or choice5 > 100)):
                    connection.send("Enter number within available number of seats:".encode(FORMAT))
                    choice5 = int(connection.recv(SIZE).decode(FORMAT))
                value4 = str(300*choice4)
                value5 = str(300*choice5)
                if(choice4 < 0 or choice4 > 100):
                    choice5 = str(choice5)
                    # ticket.write("Number of tickets booked: "+choice5+" \n")
                    nooftickets = "\nNumber of tickets booked: "+choice5
                    # ticket.write("Cost of " +choice5+ " tickets: Rs. "+ value5 +"\n")
                    cost = "\nCost of " +choice5+ " tickets: Rs. "+ value5
                else:
                    choice4 = str(choice4)
                    # ticket.write("Number of tickets booked:"+ choice4+ "\n")
                    # ticket.write("Cost of "+choice4+" tickets: Rs. "+ value4 +"\n")
                    nooftickets = "\nNumber of tickets booked: "+choice4
                    cost = "\nCost of " + choice4 + " tickets: Rs. "+ value4
                # connection.send("ticket.txt".encode(FORMAT))
                # data = ticket.read()
                # print(data)
                # connection.send(data.encode(FORMAT))
                # connection.send("Data sent Successfully".encode(FORMAT))
                connection.send("Would you like to confirm booking?['yes' or 'no']".encode(FORMAT))
                choice6 = connection.recv(SIZE).decode(FORMAT)
                if(choice6 == 'yes'):
                    connection.send(heading.encode(FORMAT))
                    connection.send(name1.encode(FORMAT))
                    connection.send(place.encode(FORMAT))
                    connection.send(theatre.encode(FORMAT))
                    connection.send(movie.encode(FORMAT))
                    connection.send(nooftickets.encode(FORMAT))
                    connection.send(cost.encode(FORMAT))
                    connection.send("\nTicket Booked Successfully\nThank You for visiting LHN Movie Booking".encode(FORMAT))
                else:
                    connection.send("\nThank You for visiting LHN Movie Booking".encode(FORMAT))
            
            else:
                # ticket.write("Movie : James \n")
                movie = "\nMovie : James"
                seat = str(seat223)
                connection.send("Available Seats: ".encode(FORMAT))
                connection.send(seat.encode(FORMAT))
                connection.send("\nCost of the ticket : Rs.300/ticket\nEnter the number of seats to be booked:".encode(FORMAT))
                
                choice4 = int(connection.recv(SIZE).decode(FORMAT))
                choice5 = -1
                while((choice4 < 0 or choice4 > 100)and(choice5 < 0 or choice5 > 100)):
                    connection.send("Enter number within available number of seats:".encode(FORMAT))
                    choice5 = int(connection.recv(SIZE).decode(FORMAT))
                value4 = str(300*choice4)
                value5 = str(300*choice5)
                if(choice4 < 0 or choice4 > 100):
                    choice5 = str(choice5)
                    # ticket.write("Number of tickets booked: "+choice5+" \n")
                    nooftickets = "\nNumber of tickets booked: "+choice5
                    # ticket.write("Cost of " +choice5+ " tickets: Rs. "+ value5 +"\n")
                    cost = "\nCost of " +choice5+ " tickets: Rs. "+ value5
                else:
                    choice4 = str(choice4)
                    # ticket.write("Number of tickets booked:"+ choice4+ "\n")
                    # ticket.write("Cost of "+choice4+" tickets: Rs. "+ value4 +"\n")
                    nooftickets = "\nNumber of tickets booked: "+choice4
                    cost = "\nCost of " + choice4 + " tickets: Rs. "+ value4
                # connection.send("ticket.txt".encode(FORMAT))
                # data = ticket.read()
                # print(data)
                # connection.send(data.encode(FORMAT))
                # connection.send("Data sent Successfully".encode(FORMAT))
                connection.send("Would you like to confirm booking?['yes' or 'no']".encode(FORMAT))
                choice6 = connection.recv(SIZE).decode(FORMAT)
                if(choice6 == 'yes'):
                    connection.send(heading.encode(FORMAT))
                    connection.send(name1.encode(FORMAT))
                    connection.send(place.encode(FORMAT))
                    connection.send(theatre.encode(FORMAT))
                    connection.send(movie.encode(FORMAT))
                    connection.send(nooftickets.encode(FORMAT))
                    connection.send(cost.encode(FORMAT))
                    connection.send("\nTicket Booked Successfully\nThank You for visiting LHN Movie Booking".encode(FORMAT))
                else:
                    connection.send("\nThank You for visiting LHN Movie Booking".encode(FORMAT))
        
    # print("[RECV] Filename received")
    # file = open("serverdata/"+filename, "w")
    # connection.send("Filename received".encode(FORMAT))

    # data = connection.recv(SIZE).decode(FORMAT)
    # print(f"[RECV] File data received")
    # file.write(data)
    # connection.send("File data received".encode(FORMAT))

    # ticket.close()
    # connection.close()
    # print(f"[DISCONNECTED] {addr} disconnected.")
    connection.close()
              
       
while True:
    Client, address = server.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
server.close() 

