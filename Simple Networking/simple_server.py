# 5/20/2026
# Creates a server, allows 2 connections from other computers, and sends those computers the message 'go' to trigger something before closing the server

import socket

host = ""
port = 9999
socket = socket.socket()

# Bind to socket
socket.bind((host,port))
socket.listen()

# Accept (2 connection)
connection,address = socket.accept()
print(f"Connection established: {address}")
connection2,address2 = socket.accept()
print(f"Connection established: {address2}")

# Send data
command = input("Type 'go' to start:")
connection.send(str.encode(command))
connection2.send(str.encode(command))
import test_flight   # insert name of file to be executed
connection.close()
connection2.close()
socket.close()
print("connection was closed")
