import socket, sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

svr_addr = ("localhost", 4444)

sock.bind(svr_addr)

# enable server to only allow 1 connection at a time
sock.listen(1)

print(f"Server started on {svr_addr[0]} port {svr_addr[1]} . . .")

connection, client_addr = sock.accept()
print(f"Connection received from {client_addr}")

while True:
    # Receive up to 1024 bytes of incoming data from one client.
    data = connection.recv(1024)
    if data:
        # decode (translate) bytes of computer code to a string value, 
        # 'open the envelope, read the letter'
        received_message = data.decode().strip().lower()
        print(f"Client says: {received_message}")
        
        if received_message == "bye":
            print("Client ended the conversation.")
            response = "Server shutdown!"
            connection.sendall(response.encode())
            break


        match received_message:
            case "cowboys":
                response = "The Cowboys are in Dallas"
            case "giants":
                response = "The Giants are in New York"
            case "eagles":
                response = "The Eagles are in Philadelphia"
            case "commanders":
                response = "The Commanders are in Washington"
            case _:
                response = "I don't know that one."

        # translate (encode) string values to bytes
        # of computer code,
        # 'pack your letter into an envelope'
        reply = response.encode()

        # Send all of the data (not just part of it) to the connected client.
        connection.sendall(reply)
    else:
        continue