# 5/19/26
# client file that receives an instruction to run choreography file

import socket
import drone_choreography   # import name of file that contains choreography code

# Connect to the socket that the server is using
HOST = "10.197.228.127" # server computer's ip
PORT = 9999 # server computer's port
s = socket.socket()
s.connect((HOST,PORT))
print("Connected.")

# Loop to constantly listen for messages
# if the message is "run", run file we imported;
# if the message is "exit", break out of loop
# else if the message is something else, print the message
while True:
    data = s.recv(1024)
    message = data.decode("utf-8")
    if message == "run":
        print("Running file.")
        drone_choreography.main()
    elif message == "exit":
        break
    else:
        print(message)
# When loop stops, close connection
s.close()
print("Connection closed.")
