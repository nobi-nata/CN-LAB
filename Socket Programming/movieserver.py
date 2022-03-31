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
    global seat111
    global seat112
    global seat113
    global seat121
    global seat122
    global seat123
    global seat211
    global seat212
    global seat213
    global seat221
    global seat222
    global seat223
    seat_check = 0

    heading = "-----------MOVIE TICKET------------"
    connection.send("-------------------LHN MOVIE BOOKING SYSTEM--------------------\n".encode(FORMAT))
    connection.send("Enter Your Name : ".encode(FORMAT))
    name = connection.recv(SIZE).decode(FORMAT)
    #nameing condition
    if name.isalpha():
        name1 = "Name : " + name
    else:
        connection.send("Enter Name with only alphabets: ".encode(FORMAT))
        name = connection.recv(SIZE).decode(FORMAT)
        name1 = "Name : " + name
    
    connection.send("Enter the date[dd/mm/yyyy] : ".encode(FORMAT))
    date = connection.recv(SIZE).decode(FORMAT)
    date1 = "\nDate : "+ date
    connection.send("Select the place:\n1.Banashankari \n2.Hosekerahalli".encode(FORMAT))
    choice1 = int(connection.recv(SIZE).decode(FORMAT))
    if choice1 == 1:
        
        place = "\nPlace : Banashankari "
        connection.send("Select the theatre:\n1.Gopalan Mall \n2.Orien Mall".encode(FORMAT))
        choice2 = int(connection.recv(SIZE).decode(FORMAT))
        if choice2 == 1:
            
            theatre = "\nTheatre : Gopalan Mall "
            connection.send("Select the movie:\n1.Kashmir Files \n2.Radhe Shyam \n3.James".encode(FORMAT))
            choice3 = int(connection.recv(SIZE).decode(FORMAT))
            if choice3 == 1:
                seat = str(seat111)
                connection.send("Available Seats: ".encode(FORMAT))
                connection.send(seat.encode(FORMAT))
                movie = "\nMovie : Kashmir Files"
                connection.send("\nCost of the ticket : Rs.300/ticket\nEnter the number of seats to be booked:".encode(FORMAT))
                choice4 = connection.recv(SIZE).decode(FORMAT)
                if choice4.isnumeric()== False:
                    connection.send("Enter valid numeric integer value :".encode(FORMAT))
                    choice4 = connection.recv(SIZE).decode(FORMAT)
                choice4 = int(choice4)
                choice5 = -1
                while((choice4 < 0 or choice4 > seat111)and(choice5 < 0 or choice5 > seat111)):
                    connection.send("Enter number within available number of seats:".encode(FORMAT))
                    choice5 = int(connection.recv(SIZE).decode(FORMAT))
                value4 = str(300*choice4)
                value5 = str(300*choice5)
                if(choice4 < 0 or choice4 > seat111):
                    seat_check = choice5
                    choice5 = str(choice5)
                    nooftickets = "\nNumber of tickets booked: "+choice5
                    cost = "\nCost of " +choice5+ " tickets: Rs. "+ value5 
                else:
                    seat_check = choice4
                    choice4 = str(choice4)
                    nooftickets = "\nNumber of tickets booked: "+choice4
                    cost = "\nCost of " + choice4 + " tickets: Rs. "+ value4
                
                connection.send("Would you like to confirm booking?['yes' or 'no']".encode(FORMAT))
                choice6 = connection.recv(SIZE).decode(FORMAT)
                if(choice6 == 'yes'):
                    seat111 -= seat_check
                    connection.send(heading.encode(FORMAT))
                    connection.send(name1.encode(FORMAT))
                    connection.send(date1.encode(FORMAT))
                    connection.send(place.encode(FORMAT))
                    connection.send(theatre.encode(FORMAT))
                    connection.send(movie.encode(FORMAT))
                    connection.send(nooftickets.encode(FORMAT))
                    connection.send(cost.encode(FORMAT))
                    connection.send("\nTicket Booked Successfully\nThank You for visiting LHN Movie Booking".encode(FORMAT))
                else:
                    connection.send("\nThank You for visiting LHN Movie Booking".encode(FORMAT))
            elif choice3 == 2:
                movie = "\nMovie : Radhe Shyam"
                seat = str(seat112)
                connection.send("Available Seats: ".encode(FORMAT))
                connection.send(seat.encode(FORMAT))
                connection.send("\nCost of the ticket : Rs.300/ticket\nEnter the number of seats to be booked:".encode(FORMAT))
                
                choice4 = int(connection.recv(SIZE).decode(FORMAT))
                choice5 = -1
                while((choice4 < 0 or choice4 > seat112)and(choice5 < 0 or choice5 > seat112)):
                    connection.send("Enter number within available number of seats:".encode(FORMAT))
                    choice5 = int(connection.recv(SIZE).decode(FORMAT))
                value4 = str(300*choice4)
                value5 = str(300*choice5)
                if(choice4 < 0 or choice4 > seat112):
                    seat_check = choice5
                    choice5 = str(choice5)
                    nooftickets = "\nNumber of tickets booked: "+choice5
                    cost = "\nCost of " +choice5+ " tickets: Rs. "+ value5
                else:
                    seat_check = choice4
                    choice4 = str(choice4)
                    nooftickets = "\nNumber of tickets booked: "+choice4
                    cost = "\nCost of " + choice4 + " tickets: Rs. "+ value4
                connection.send("Would you like to confirm booking?['yes' or 'no']".encode(FORMAT))
                choice6 = connection.recv(SIZE).decode(FORMAT)
                if(choice6 == 'yes'):
                    seat112 -= seat_check
                    connection.send(heading.encode(FORMAT))
                    connection.send(name1.encode(FORMAT))
                    connection.send(date1.encode(FORMAT))
                    connection.send(place.encode(FORMAT))
                    connection.send(theatre.encode(FORMAT))
                    connection.send(movie.encode(FORMAT))
                    connection.send(nooftickets.encode(FORMAT))
                    connection.send(cost.encode(FORMAT))
                    connection.send("\nTicket Booked Successfully\nThank You for visiting LHN Movie Booking".encode(FORMAT))
                else:
                    connection.send("\nThank You for visiting LHN Movie Booking".encode(FORMAT))
            
            else:
                movie = "\nMovie : James"
                seat = str(seat113)
                connection.send("Available Seats: ".encode(FORMAT))
                connection.send(seat.encode(FORMAT))
                connection.send("\nCost of the ticket : Rs.300/ticket\nEnter the number of seats to be booked:".encode(FORMAT))
                
                choice4 = int(connection.recv(SIZE).decode(FORMAT))
                choice5 = -1
                while((choice4 < 0 or choice4 > seat113)and(choice5 < 0 or choice5 > seat113)):
                    connection.send("Enter number within available number of seats:".encode(FORMAT))
                    choice5 = int(connection.recv(SIZE).decode(FORMAT))
                value4 = str(300*choice4)
                value5 = str(300*choice5)
                if(choice4 < 0 or choice4 > seat113):
                    seat_check = choice5
                    choice5 = str(choice5)
                    nooftickets = "\nNumber of tickets booked: "+choice5
                    cost = "\nCost of " +choice5+ " tickets: Rs. "+ value5
                else:
                    seat_check = choice4
                    choice4 = str(choice4)
                    nooftickets = "\nNumber of tickets booked: "+choice4
                    cost = "\nCost of " + choice4 + " tickets: Rs. "+ value4
                connection.send("Would you like to confirm booking?['yes' or 'no']".encode(FORMAT))
                choice6 = connection.recv(SIZE).decode(FORMAT)
                if(choice6 == 'yes'):
                    seat113 -= seat_check
                    connection.send(heading.encode(FORMAT))
                    connection.send(name1.encode(FORMAT))
                    connection.send(date1.encode(FORMAT))
                    connection.send(place.encode(FORMAT))
                    connection.send(theatre.encode(FORMAT))
                    connection.send(movie.encode(FORMAT))
                    connection.send(nooftickets.encode(FORMAT))
                    connection.send(cost.encode(FORMAT))
                    connection.send("\nTicket Booked Successfully\nThank You for visiting LHN Movie Booking".encode(FORMAT))
                else:
                    connection.send("\nThank You for visiting LHN Movie Booking".encode(FORMAT))
        else:
            theatre = "\nTheatre : Orien Mall"
            connection.send("Select the movie:\n1.Kashmir Files \n2.Radhe Shyam \n3.James".encode(FORMAT))
            choice3 = int(connection.recv(SIZE).decode(FORMAT))
            if choice3 == 1:
                movie = "\nMovie : Kashmir Files"
                seat = str(seat121)
                connection.send("Available Seats: ".encode(FORMAT))
                connection.send(seat.encode(FORMAT))
                connection.send("\nCost of the ticket : Rs.300/ticket\nEnter the number of seats to be booked:".encode(FORMAT))
                
                choice4 = int(connection.recv(SIZE).decode(FORMAT))
                choice5 = -1
                while((choice4 < 0 or choice4 > seat121)and(choice5 < 0 or choice5 > seat121)):
                    connection.send("Enter number within available number of seats:".encode(FORMAT))
                    choice5 = int(connection.recv(SIZE).decode(FORMAT))
                value4 = str(300*choice4)
                value5 = str(300*choice5)
                if(choice4 < 0 or choice4 > seat121):
                    seat_check = choice5
                    choice5 = str(choice5)
                    nooftickets = "\nNumber of tickets booked: "+choice5
                    cost = "\nCost of " +choice5+ " tickets: Rs. "+ value5
                else:
                    seat_check = choice4
                    choice4 = str(choice4)
                    nooftickets = "\nNumber of tickets booked: "+choice4
                    cost = "\nCost of " + choice4 + " tickets: Rs. "+ value4
                connection.send("Would you like to confirm booking?['yes' or 'no']".encode(FORMAT))
                choice6 = connection.recv(SIZE).decode(FORMAT)
                if(choice6 == 'yes'):
                    seat121 -= seat_check
                    connection.send(heading.encode(FORMAT))
                    connection.send(name1.encode(FORMAT))
                    connection.send(date1.encode(FORMAT))
                    connection.send(place.encode(FORMAT))
                    connection.send(theatre.encode(FORMAT))
                    connection.send(movie.encode(FORMAT))
                    connection.send(nooftickets.encode(FORMAT))
                    connection.send(cost.encode(FORMAT))
                    connection.send("\nTicket Booked Successfully\nThank You for visiting LHN Movie Booking".encode(FORMAT))
                else:
                    connection.send("\nThank You for visiting LHN Movie Booking".encode(FORMAT))
            elif choice3 == 2:
                movie = "\nMovie : Radhe Shyam"
                seat = str(seat122)
                connection.send("Available Seats: ".encode(FORMAT))
                connection.send(seat.encode(FORMAT))
                connection.send("\nCost of the ticket : Rs.300/ticket\nEnter the number of seats to be booked:".encode(FORMAT))
                
                choice4 = int(connection.recv(SIZE).decode(FORMAT))
                choice5 = -1
                while((choice4 < 0 or choice4 > seat122)and(choice5 < 0 or choice5 > seat122)):
                    connection.send("Enter number within available number of seats:".encode(FORMAT))
                    choice5 = int(connection.recv(SIZE).decode(FORMAT))
                value4 = str(300*choice4)
                value5 = str(300*choice5)
                if(choice4 < 0 or choice4 > seat122):
                    seat_check = choice5
                    choice5 = str(choice5)
                    nooftickets = "\nNumber of tickets booked: "+choice5
                    cost = "\nCost of " +choice5+ " tickets: Rs. "+ value5
                else:
                    seat_check = choice4
                    choice4 = str(choice4)
                    nooftickets = "\nNumber of tickets booked: "+choice4
                    cost = "\nCost of " + choice4 + " tickets: Rs. "+ value4
                connection.send("Would you like to confirm booking?['yes' or 'no']".encode(FORMAT))
                choice6 = connection.recv(SIZE).decode(FORMAT)
                if(choice6 == 'yes'):
                    seat122 -= seat_check
                    connection.send(heading.encode(FORMAT))
                    connection.send(name1.encode(FORMAT))
                    connection.send(date1.encode(FORMAT))
                    connection.send(place.encode(FORMAT))
                    connection.send(theatre.encode(FORMAT))
                    connection.send(movie.encode(FORMAT))
                    connection.send(nooftickets.encode(FORMAT))
                    connection.send(cost.encode(FORMAT))
                    connection.send("\nTicket Booked Successfully\nThank You for visiting LHN Movie Booking".encode(FORMAT))
                else:
                    connection.send("\nThank You for visiting LHN Movie Booking".encode(FORMAT))
            else:
                movie = "\nMovie : James"
                seat = str(seat123)
                connection.send("Available Seats: ".encode(FORMAT))
                connection.send(seat.encode(FORMAT))
                connection.send("\nCost of the ticket : Rs.300/ticket\nEnter the number of seats to be booked:".encode(FORMAT))
                
                choice4 = int(connection.recv(SIZE).decode(FORMAT))
                choice5 = -1
                while((choice4 < 0 or choice4 > seat123)and(choice5 < 0 or choice5 > seat123)):
                    connection.send("Enter number within available number of seats:".encode(FORMAT))
                    choice5 = int(connection.recv(SIZE).decode(FORMAT))
                value4 = str(300*choice4)
                value5 = str(300*choice5)
                if(choice4 < 0 or choice4 > seat123):
                    seat_check = choice5
                    choice5 = str(choice5)
                    nooftickets = "\nNumber of tickets booked: "+choice5
                    cost = "\nCost of " +choice5+ " tickets: Rs. "+ value5
                else:
                    seat_check = choice4
                    choice4 = str(choice4)
                    nooftickets = "\nNumber of tickets booked: "+choice4
                    cost = "\nCost of " + choice4 + " tickets: Rs. "+ value4
                connection.send("Would you like to confirm booking?['yes' or 'no']".encode(FORMAT))
                choice6 = connection.recv(SIZE).decode(FORMAT)
                if(choice6 == 'yes'):
                    seat123 -= seat_check
                    connection.send(heading.encode(FORMAT))
                    connection.send(name1.encode(FORMAT))
                    connection.send(date1.encode(FORMAT))
                    connection.send(place.encode(FORMAT))
                    connection.send(theatre.encode(FORMAT))
                    connection.send(movie.encode(FORMAT))
                    connection.send(nooftickets.encode(FORMAT))
                    connection.send(cost.encode(FORMAT))
                    connection.send("\nTicket Booked Successfully\nThank You for visiting LHN Movie Booking".encode(FORMAT))
                else:
                    connection.send("\nThank You for visiting LHN Movie Booking".encode(FORMAT))
    
    
    else:
        place = "\nPlace : Hosekerahalli "
        connection.send("Select the theatre:\n1.Gopalan Mall \n2.Orien Mall".encode(FORMAT))
        choice2 = int(connection.recv(SIZE).decode(FORMAT))
        if choice2 == 1:
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
                while((choice4 < 0 or choice4 > seat211)and(choice5 < 0 or choice5 > seat211)):
                    connection.send("Enter number within available number of seats:".encode(FORMAT))
                    choice5 = int(connection.recv(SIZE).decode(FORMAT))
                value4 = str(300*choice4)
                value5 = str(300*choice5)
                if(choice4 < 0 or choice4 > seat211):
                    seat_check = choice5
                    choice5 = str(choice5)
                    nooftickets = "\nNumber of tickets booked: "+choice5
                    cost = "\nCost of " +choice5+ " tickets: Rs. "+ value5
                else:
                    seat_check = choice4
                    choice4 = str(choice4)
                    nooftickets = "\nNumber of tickets booked: "+choice4
                    cost = "\nCost of " + choice4 + " tickets: Rs. "+ value4
                connection.send("Would you like to confirm booking?['yes' or 'no']".encode(FORMAT))
                choice6 = connection.recv(SIZE).decode(FORMAT)
                if(choice6 == 'yes'):
                    seat211 -= seat_check
                    connection.send(heading.encode(FORMAT))
                    connection.send(name1.encode(FORMAT))
                    connection.send(date1.encode(FORMAT))
                    connection.send(place.encode(FORMAT))
                    connection.send(theatre.encode(FORMAT))
                    connection.send(movie.encode(FORMAT))
                    connection.send(nooftickets.encode(FORMAT))
                    connection.send(cost.encode(FORMAT))
                    connection.send("\nTicket Booked Successfully\nThank You for visiting LHN Movie Booking".encode(FORMAT))
                else:
                    connection.send("\nThank You for visiting LHN Movie Booking".encode(FORMAT))
            
            elif choice3 == 2:
                movie = "\nMovie : Radhe Shyam"
                seat = str(seat212)
                connection.send("Available Seats: ".encode(FORMAT))
                connection.send(seat.encode(FORMAT))
                connection.send("\nCost of the ticket : Rs.300/ticket\nEnter the number of seats to be booked:".encode(FORMAT))
                
                choice4 = int(connection.recv(SIZE).decode(FORMAT))
                choice5 = -1
                while((choice4 < 0 or choice4 > seat212)and(choice5 < 0 or choice5 > seat212)):
                    connection.send("Enter number within available number of seats:".encode(FORMAT))
                    choice5 = int(connection.recv(SIZE).decode(FORMAT))
                value4 = str(300*choice4)
                value5 = str(300*choice5)
                if(choice4 < 0 or choice4 > seat212):
                    seat_check = choice5
                    choice5 = str(choice5)
                    nooftickets = "\nNumber of tickets booked: "+choice5
                    cost = "\nCost of " +choice5+ " tickets: Rs. "+ value5
                else:
                    seat_check = choice4
                    choice4 = str(choice4)
                    nooftickets = "\nNumber of tickets booked: "+choice4
                    cost = "\nCost of " + choice4 + " tickets: Rs. "+ value4
                connection.send("Would you like to confirm booking?['yes' or 'no']".encode(FORMAT))
                choice6 = connection.recv(SIZE).decode(FORMAT)
                if(choice6 == 'yes'):
                    seat212 -= seat_check
                    connection.send(heading.encode(FORMAT))
                    connection.send(name1.encode(FORMAT))
                    connection.send(date1.encode(FORMAT))
                    connection.send(place.encode(FORMAT))
                    connection.send(theatre.encode(FORMAT))
                    connection.send(movie.encode(FORMAT))
                    connection.send(nooftickets.encode(FORMAT))
                    connection.send(cost.encode(FORMAT))
                    connection.send("\nTicket Booked Successfully\nThank You for visiting LHN Movie Booking".encode(FORMAT))
                else:
                    connection.send("\nThank You for visiting LHN Movie Booking".encode(FORMAT))
            
            else:
                movie = "\nMovie : James"
                seat = str(seat213)
                connection.send("Available Seats: ".encode(FORMAT))
                connection.send(seat.encode(FORMAT))
                connection.send("\nCost of the ticket : Rs.300/ticket\nEnter the number of seats to be booked:".encode(FORMAT))
                
                choice4 = int(connection.recv(SIZE).decode(FORMAT))
                choice5 = -1
                while((choice4 < 0 or choice4 > seat213)and(choice5 < 0 or choice5 > seat213)):
                    connection.send("Enter number within available number of seats:".encode(FORMAT))
                    choice5 = int(connection.recv(SIZE).decode(FORMAT))
                value4 = str(300*choice4)
                value5 = str(300*choice5)
                if(choice4 < 0 or choice4 > seat213):
                    seat_check = choice5
                    choice5 = str(choice5)
                    nooftickets = "\nNumber of tickets booked: "+choice5
                    cost = "\nCost of " +choice5+ " tickets: Rs. "+ value5
                else:
                    seat_check = choice4
                    choice4 = str(choice4)
                    nooftickets = "\nNumber of tickets booked: "+choice4
                    cost = "\nCost of " + choice4 + " tickets: Rs. "+ value4
                connection.send("Would you like to confirm booking?['yes' or 'no']".encode(FORMAT))
                choice6 = connection.recv(SIZE).decode(FORMAT)
                if(choice6 == 'yes'):
                    seat213 -= seat_check
                    connection.send(heading.encode(FORMAT))
                    connection.send(name1.encode(FORMAT))
                    connection.send(date1.encode(FORMAT))
                    connection.send(place.encode(FORMAT))
                    connection.send(theatre.encode(FORMAT))
                    connection.send(movie.encode(FORMAT))
                    connection.send(nooftickets.encode(FORMAT))
                    connection.send(cost.encode(FORMAT))
                    connection.send("\nTicket Booked Successfully\nThank You for visiting LHN Movie Booking".encode(FORMAT))
                else:
                    connection.send("\nThank You for visiting LHN Movie Booking".encode(FORMAT))
            
        else:
            theatre = "\nTheatre : Orien Mall"
            connection.send("Select the movie:\n1.Kashmir Files \n2.Radhe Shyam \n3.James".encode(FORMAT))
            choice3 = int(connection.recv(SIZE).decode(FORMAT))
            if choice3 == 1:
                movie = "\nMovie : Kashmir Files"
                seat = str(seat221)
                connection.send("Available Seats: ".encode(FORMAT))
                connection.send(seat.encode(FORMAT))
                connection.send("\nCost of the ticket : Rs.300/ticket\nEnter the number of seats to be booked:".encode(FORMAT))
                
                choice4 = int(connection.recv(SIZE).decode(FORMAT))
                choice5 = -1
                while((choice4 < 0 or choice4 > seat221)and(choice5 < 0 or choice5 > seat221)):
                    connection.send("Enter number within available number of seats:".encode(FORMAT))
                    choice5 = int(connection.recv(SIZE).decode(FORMAT))
                value4 = str(300*choice4)
                value5 = str(300*choice5)
                if(choice4 < 0 or choice4 > seat221):
                    seat_check = choice5
                    choice5 = str(choice5)
                    nooftickets = "\nNumber of tickets booked: "+choice5
                    cost = "\nCost of " +choice5+ " tickets: Rs. "+ value5
                else:
                    seat_check = choice4
                    choice4 = str(choice4)
                    nooftickets = "\nNumber of tickets booked: "+choice4
                    cost = "\nCost of " + choice4 + " tickets: Rs. "+ value4
                connection.send("Would you like to confirm booking?['yes' or 'no']".encode(FORMAT))
                choice6 = connection.recv(SIZE).decode(FORMAT)
                if(choice6 == 'yes'):
                    seat221 -= seat_check
                    connection.send(heading.encode(FORMAT))
                    connection.send(name1.encode(FORMAT))
                    connection.send(date1.encode(FORMAT))
                    connection.send(place.encode(FORMAT))
                    connection.send(theatre.encode(FORMAT))
                    connection.send(movie.encode(FORMAT))
                    connection.send(nooftickets.encode(FORMAT))
                    connection.send(cost.encode(FORMAT))
                    connection.send("\nTicket Booked Successfully\nThank You for visiting LHN Movie Booking".encode(FORMAT))
                else:
                    connection.send("\nThank You for visiting LHN Movie Booking".encode(FORMAT))
                            
            elif choice3 == 2:
                movie = "\nMovie : Radhe Shyam"
                seat = str(seat222)
                connection.send("Available Seats: ".encode(FORMAT))
                connection.send(seat.encode(FORMAT))
                connection.send("\nCost of the ticket : Rs.300/ticket\nEnter the number of seats to be booked:".encode(FORMAT))
                
                choice4 = int(connection.recv(SIZE).decode(FORMAT))
                choice5 = -1
                while((choice4 < 0 or choice4 > seat222)and(choice5 < 0 or choice5 > seat222)):
                    connection.send("Enter number within available number of seats:".encode(FORMAT))
                    choice5 = int(connection.recv(SIZE).decode(FORMAT))
                value4 = str(300*choice4)
                value5 = str(300*choice5)
                if(choice4 < 0 or choice4 > seat222):
                    seat_check = choice5
                    choice5 = str(choice5)
                    nooftickets = "\nNumber of tickets booked: "+choice5
                    cost = "\nCost of " +choice5+ " tickets: Rs. "+ value5
                else:
                    seat_check = choice4
                    choice4 = str(choice4)
                    nooftickets = "\nNumber of tickets booked: "+choice4
                    cost = "\nCost of " + choice4 + " tickets: Rs. "+ value4
                connection.send("Would you like to confirm booking?['yes' or 'no']".encode(FORMAT))
                choice6 = connection.recv(SIZE).decode(FORMAT)
                if(choice6 == 'yes'):
                    seat222 -= seat_check
                    connection.send(heading.encode(FORMAT))
                    connection.send(name1.encode(FORMAT))
                    connection.send(date1.encode(FORMAT))
                    connection.send(place.encode(FORMAT))
                    connection.send(theatre.encode(FORMAT))
                    connection.send(movie.encode(FORMAT))
                    connection.send(nooftickets.encode(FORMAT))
                    connection.send(cost.encode(FORMAT))
                    connection.send("\nTicket Booked Successfully\nThank You for visiting LHN Movie Booking".encode(FORMAT))
                else:
                    connection.send("\nThank You for visiting LHN Movie Booking".encode(FORMAT))
            
            else:
                movie = "\nMovie : James"
                seat = str(seat223)
                connection.send("Available Seats: ".encode(FORMAT))
                connection.send(seat.encode(FORMAT))
                connection.send("\nCost of the ticket : Rs.300/ticket\nEnter the number of seats to be booked:".encode(FORMAT))
                
                choice4 = int(connection.recv(SIZE).decode(FORMAT))
                choice5 = -1
                while((choice4 < 0 or choice4 > seat223)and(choice5 < 0 or choice5 > seat223)):
                    connection.send("Enter number within available number of seats:".encode(FORMAT))
                    choice5 = int(connection.recv(SIZE).decode(FORMAT))
                value4 = str(300*choice4)
                value5 = str(300*choice5)
                if(choice4 < 0 or choice4 > seat223):
                    seat_check = choice5
                    choice5 = str(choice5)
                    nooftickets = "\nNumber of tickets booked: "+choice5
                    cost = "\nCost of " +choice5+ " tickets: Rs. "+ value5
                else:
                    seat_check = choice4
                    choice4 = str(choice4)
                    nooftickets = "\nNumber of tickets booked: "+choice4
                    cost = "\nCost of " + choice4 + " tickets: Rs. "+ value4
                connection.send("Would you like to confirm booking?['yes' or 'no']".encode(FORMAT))
                choice6 = connection.recv(SIZE).decode(FORMAT)
                if(choice6 == 'yes'):
                    seat223 -= seat_check
                    connection.send(heading.encode(FORMAT))
                    connection.send(name1.encode(FORMAT))
                    connection.send(date1.encode(FORMAT))
                    connection.send(place.encode(FORMAT))
                    connection.send(theatre.encode(FORMAT))
                    connection.send(movie.encode(FORMAT))
                    connection.send(nooftickets.encode(FORMAT))
                    connection.send(cost.encode(FORMAT))
                    connection.send("\nTicket Booked Successfully\nThank You for visiting LHN Movie Booking".encode(FORMAT))
                else:
                    connection.send("\nThank You for visiting LHN Movie Booking".encode(FORMAT))
        
    connection.close()
              
       
while True:
    Client, address = server.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
server.close() 

