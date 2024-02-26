import socket
import json
from Inventory_models.models import Recieved_data,line_graph_data

def receive_and_print_data(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break  # Break the loop if no more data is received
            # print({data})

            json_data = json.loads(data)
            # line_graph=line_graph_data.objects.all()
            received_data_instance=Recieved_data.objects.all()

            line_graph = line_graph_data(
                tag1=json_data.get('tag1', 0),
                tag2=json_data.get('tag2', 0),
                tag3=json_data.get('tag3', 0),
                tag4=json_data.get('tag4', 0),
                tag5=json_data.get('tag5', 0),
                tag6=json_data.get('tag6', 0),
                tag7=json_data.get('tag7', 0),
                tag8=json_data.get('tag8', 0),
            )
            line_graph.save()

            if len(received_data_instance) != 0:
                received_data_instance.delete()
            # a=[Recieved_data]

            # json_data = json.loads(data)
            received_data_instance = Recieved_data(
                tag1=json_data.get('tag1', 0),
                tag2=json_data.get('tag2', 0),
                tag3=json_data.get('tag3', 0),
                tag4=json_data.get('tag4', 0),
                tag5=json_data.get('tag5', 0),
                tag6=json_data.get('tag6', 0),
                tag7=json_data.get('tag7', 0),
                tag8=json_data.get('tag8', 0),
            )

            # Save the instance to the database
            received_data_instance.save()
    finally:
        client_socket.close()

if __name__ == "__main__":
    host = '192.168.1.16'  # Replace with the actual IP address of your server machine
    port = 12356  # Use the same port number you specified in the server code

    receive_and_print_data(host, port)
