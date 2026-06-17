# 5/19/2026
# Server file that uses threading and sends command to all clients to code.

import socket
import threading
import subprocess
import sys
from pathlib import Path
grandparent_dir = str(Path(__file__).resolve().parent.parent)
print(grandparent_dir)
file = 'EXAMPLE.py'

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
    msg = input("Type 'run', 'file', or 'exit': ")
    msg = msg.lower()
    if msg == 'exit':
        break
    if msg == 'run':
        send_command(msg)
        print("Running file. File Output:\n")
        subprocess.run([sys.executable, file])   # fancy way to execute file
        print("\n")
    if msg == 'file':
        send_command(msg)
        file = input("Insert name of file being run (with .py): ")
        file_msg = file.removeprefix(grandparent_dir)
        print(f"File suffix is: {file_msg}")
        send_command(file_msg)
server.close()
