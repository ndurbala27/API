import socket, sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

svr_addr = ("localhost", 4444)

sock.bind(svr_addr)

sock.listen(1)

print(f"Server started on {svr_addr[0]} port {svr_addr[1]} . . .")

while True:
    connection, client_addr = sock.accept()
    print(f"Connection received from {client_addr}")
    try:
        while True:
            data = connection.recv(1024)
            if data:
                #print(f"Received: {data.decode()}")
                msg = f"Hello, {data.decode()}!"

                match received_message:
                    case "cowboys":
                        response = "Dallas"
                    case "giants":
                        response = "New York"
                    case "eagles":
                        response = "Philadelphia"
                    case "commanders":
                        response = "Washington"
                    case _:
                        response = "I don't know that one."


                connection.sendall(msg.encode())
                #print(f"Sent: {data.decode()}")
            else:
                break
    except KeyboardInterrupt:
        connection.close()
        break