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

# Step 3: Send data
command = input("Type 'go' to start:")
connection.send(str.encode(command))
connection2.send(str.encode(command))
connection3.send(str.encode(command))
print("Waiting for response")
if str(connection.recv(1024),"utf-8") == str(connection2.recv(1024),"utf-8") == str(connection3.recv(1024),"utf-8") == 'received':
    import name   # insert name of file to be executed
    connection.close()
    socket.close()
    print("connection was closed")
