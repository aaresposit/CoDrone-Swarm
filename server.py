# 5/18/2026
# Server file that sends command to all clients to run their choreography files and runs its own.

# Step 1: Set up socket
import socket
HOST = ""
PORT = 9999
s = socket.socket()
s.bind((HOST,PORT))
s.listen()


# Step 2: Accept Connections
print("How many computers will connect to this one?")
# Loop and get user input
# If whole number greater than 0, break out of loop
while True:
    try:
        amount_connecting = int(input("Enter a whole number greater than zero:"))
        if amount_connecting > 0:
            break
    except:
        pass
# Begin to connect to computers
# Create lists to store info
print(f"Okay, waiting for {amount_connecting} computers to connect.")
connections = []
addresses = []
# For each of the # of computers: connect to a computer, store its information, and tell it which number it is
for computer in range(amount_connecting):
    connection,address = s.accept()
    connections.append(connection)
    addresses.append(address)
    print(f"Connection {computer+1} established: {address}")
    message = f"This computer is connection {computer+1}."
    connection.send(message.encode("utf-8"))


# Step 3: Send data
while True:
    message = input("Type 'run' to run choreography files, or 'exit' to disconnect all computers: ")
    message = message.lower()
    for conn,addr in zip(connections,addresses):
        try:
            conn.send(message.encode("utf-8"))
            if message == "exit":
                conn.close()
        except:
            print(f"Could not send to {addr}. Check client computer.")
    if message == "run":
        drone_choreography.main()   # same name as import with .main() attached to end
s.close()
print("Connection was closed.")
