# 5/18/26
# client file that receives an instruction to run choreography file

import socket

HOST = "192.168.0.196" # server computer's ip
PORT = 9999 # server port
s = socket.socket()

s.connect((HOST,PORT))
print("Connected")

while True:
    data = s.recv(1024)
    command = data.decode("utf-8")
    if command == "go":
        reply = "received"
        s.send(reply.encode("utf-8"))
        print("Running file.")
        import test_flight   # insert name of file to run here
        s.close()
