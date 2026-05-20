# 5/20/26
# Connects to a server (host, port), waits for a message "go" from the server, and once received imports a file (which runs it) and closes the socket object 

import socket

host = "192.168.0.0" # server computer's ip
port = 9999 # server port
socket = socket.socket()

socket.connect((host,port))
print("Connected")

while True:
    data = socket.recv(1024)
    message = data.decode("utf-8")
    if message == "go":
        print("Running file.")
        import test_flight # insert name of file to run here
        socket.close()
