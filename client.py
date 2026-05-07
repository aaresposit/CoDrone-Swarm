# 5/7/26
#

import socket

host = "192.168.0.0" # server computer's ip
port = 9999 # server port
socket = socket.socket()

socket.connect((host,port))
print("Connected")

while True:
    data = socket.recv(1024)
    command = data.decode("utf-8")
    if command == "go":
        socket.send(str.encode("received"))
        print("Running file.")
        import name   # insert name of file to run here
        socket.close()
