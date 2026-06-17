# 6/17/26
# client file that receives an instruction to run choreography file

import socket
import subprocess
import sys
from pathlib import Path
grandfather_dir = str(Path(__file__).resolve().parent.parent)
print(grandfather_dir)
file = 'EXAMPLE.py'

# Connect to the socket that the server is using
HOST = "192.168.0.162" # server computer's ip
PORT = 9999 # server computer's port
s = socket.socket()
s.connect((HOST,PORT))
print("Connected.")

# Loop to constantly listen for messages
# if the message is "run", run file we imported;
# if the message is "exit" or '', break out of loop
# else if the message is something else, print the message
receiving_file = False
while True:
    data = s.recv(1024)
    message = data.decode("utf-8")
    if receiving_file:
        if len(message) > 0:
            file = grandfather_dir + message
            print(f'File received: {file}')
            receiving_file = False
    elif message == "run":
        print("Running file. File Output:\n")
        subprocess.run([sys.executable,file])
        print("\n")
    elif message == "exit" or '':
        break
    elif message == "file":
        print('Waiting for file.')
        receiving_file = True
    else:
        print(message)
# When loop stops, close connection
s.close()
print("Connection closed.")
