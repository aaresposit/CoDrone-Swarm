# 5/7/2026
# Server file that sends command to all clients to run drone code and runs its own.

import socket

host = ""
port = 9999
socket = socket.socket()

# Step 1: Bind
def bind_socket():
    try:
        socket.bind((host,port))
        socket.listen(5)
    except:
        print("Retry bind\r")
        bind_socket()
bind_socket()

# Step 2: Accept (3 connections)
connection,address = socket.accept()
print(f"Connection established: {address}")
connection2,address2 = socket.accept()
print(f"Connection established: {address2}")
connection3,address3 = socket.accept()
print(f"Connection established: {address3}")
#connections = addresses = []
#user_input = 'yes'
#i = 0
#while user_input == 'yes' or user_input == 'y':
#    i += 1
#    connections[i],addresses[i] = socket.accept()
#    print(f"Connection established: {address[i]}")
#    user_input = input("More computers?")
    # better to learn threading?


# Step 3: Send data
command = input("Type 'go' to start:")
#for connection in connections:
#    connection.send(str.encode(command))
connection.send(str.encode(command))
connection2.send(str.encode(command))
connection3.send(str.encode(command))
print("Waiting for response")
if str(connection.recv(1024),"utf-8") == str(connection2.recv(1024),"utf-8") == str(connection3.recv(1024),"utf-8") == 'received':
    import name   # insert name of file to be executed
    connection.close()
    socket.close()
    print("connection was closed")
