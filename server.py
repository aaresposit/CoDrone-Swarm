# 5/18/2026
# Server file that sends command to all clients to run their choreography files and runs its own.

import socket
HOST = ""
PORT = 9999
s = socket.socket()


# Step 1: Bind
def bind_socket():
    try:
        s.bind((HOST,PORT))
        s.listen(5)
    except:
        print("Retry bind\r")
        bind_socket()
bind_socket()


# Step 2: Accept (3 connections)
print("How many computers will connect to this one?")
amount_connecting = None
while type(amount_connecting) != int:
    try:
        amount_connecting = int(input())
    except:
        print("Please enter a whole number.")

print(f"Okay, waiting for {amount_connecting} computers to connect.")
connections = []
addresses = []
for computer in range(amount_connecting):
    connection,address = s.accept()
    connections.append(connection)
    addresses.append(address)
    print(f"Connection established: {address}")


# Step 3: Send data
command = input("Type 'go' to start:")
for conn in connections:
    conn.send(str.encode(command))
    conn.close()
import test_flight   # insert name of file to be executed
s.close()
print("connection was closed")

