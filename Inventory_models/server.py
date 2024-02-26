import socket
import json
import random
import time

def generate_data():
    tags = ["tag1", "tag2", "tag3", "tag4", "tag5", "tag6", "tag7", "tag8"]
    data = {tag: random.randint(4, 20) for tag in tags}
    return json.dumps(data)

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        try:
            while True:
                data = generate_data()
                client_socket.send(data.encode())
                time.sleep(2)  # Delay for 2000 milliseconds before sending the next update
        except BrokenPipeError:
            # Handle the case when the client disconnects
            print(f"Client {client_address} disconnected.")
        finally:
            client_socket.close()

if __name__ == "__main__":
    host = '192.168.1.16'  # Replace with the actual IP address of your server machine
    port = 12356  # Choose a suitable port number

    start_server(host, port)
