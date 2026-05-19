# 5/19/2026
# Server file that uses threading and sends command to all clients to code.

import socket
import threading
from codrone import drone_choreography

HOST = ''
PORT = 9999
clients = []
addresses = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

def send_command(message):
    """Sends a string to all connected clients."""
    print(f"\nSending command to computers.")
    for client,address in zip(clients[:],addresses[:]): # Copy list to avoid thread conflicts
        try:
            client.send(message.encode('utf-8'))
        except:
            clients.remove(client)
            print(f"[-] Client {address[0]} disconnected. Total: {len(clients)}")

def handle_incoming_connections():
    """Runs in the background to accept new clients without blocking."""
    while True:
        try:
            client_socket, client_address = server.accept()
            clients.append(client_socket)
            addresses.append(client_address)
            print(f"\n[+] Client {client_address[0]} connected. Total: {len(clients)}")
        except:
            break

# Start the connection listener in the background
listener_thread = threading.Thread(target=handle_incoming_connections, daemon=True)
listener_thread.start()

# Main thread is now completely free to broadcast at any time
print("Server is running.")
while True:
    msg = input("Type 'run' to run choreography files, or 'exit' to disconnect all computers: ")
    msg = msg.lower()
    if msg == 'exit':
        break
    if msg == 'run':
        print("Running file.")
        send_command(msg)
        drone_choreography.main()
server.close()
