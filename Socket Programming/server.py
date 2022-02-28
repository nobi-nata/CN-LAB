import socket
from tkinter import *

def send(listbox,entry):
    message = entry.get()
    listbox.insert('end',message)
    entry.delete(0,END)
    client.send(bytes(message, "utf-8"))

def receive(listbox):
    message_from_client = client.recv(50)
    listbox.insert('end',"Client:" + message_from_client.decode('utf-8'))


root = Tk()

entry = Entry()
entry.pack(side=BOTTOM)

listbox = Listbox(root)
listbox.pack()

button = Button(root,text="SEND",command=lambda:send(listbox,entry))
button.pack(side=BOTTOM)

rbutton = Button(root, text="RECEIVE", command=lambda: receive(listbox))
rbutton.pack(side=BOTTOM)

root.title('Server')

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST_NAME = socket.gethostname()
PORT = 12345

s.bind((HOST_NAME,PORT))

s.listen(4)
client, address = s.accept()

root.mainloop()