import socket, sys

# created a TCP client and connected to local server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 4444))

teams = ['Cowboys', 'Giants', 'Eagles', 'Commanders']

print("Welcome to NFL Chatbot!")
print(f"Type one of: {", ".join(teams)}")
print("Or type anything else to see what happens, like 'bye'!")


try:
    while True:
        msg = input("Team? ")
        if msg.strip().lower() == "bye":
            print(f"Sent to server: {msg}")
            print("Goodbye!")
            sock.sendall(msg.encode())
            break
        else:
            sock.sendall(msg.encode())
            print(f"Sent to server: {msg}")
            data = sock.recv(1024)
            print(f"Server says: {data.decode()}")
finally:
    sock.close()