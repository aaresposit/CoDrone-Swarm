# 5/19/2026
# Server file that sends command to all clients to run their choreography files and runs its own.

# Step 1: Set up socket
import socket
import choreographyfilename
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
        amount_connecting = int(input("Enter a whole number greater than zero: "))
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
    conn, addr = s.accept()
    connections.append(conn)
    addresses.append(addr)
    print(f"Connection {computer+1} established: {addr}")
    message = f"This computer is connection {computer+1}."
    conn.send(message.encode("utf-8"))


# Step 3: Send data
# Loop and get user input for message sent
# Send message to every connection in the connections list; if error message, print which computer and address and remove it from connections.
# If message is "run", run choreography file
# If message is "exit", close connections and break out of loop
while True:
    message = input("Type 'run' to run choreography files, or 'exit' to disconnect all computers: ")
    message = message.lower()
    for conn, addr, computer in zip(connections, addresses, range(amount_connecting)):
        try:
            conn.send(message.encode("utf-8"))
        except:
            print(f"Could not send to connection {computer+1} at {addr}.")
            connections.remove(conn)
    if message == "run":
        choreographyfilename.main()   # same name as import with .main() attached to end
    if message == "exit":
        for conn in connections:
            conn.close()
        break
s.close()
print("Connection was closed.")
