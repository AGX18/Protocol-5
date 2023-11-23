# client.py

import socket

def send_data(sock, data):
    sock.send(data.encode())

def receive_ack(sock):
    ack = sock.recv(1024).decode()
    return ack

def client():
    server_ip = '127.0.0.1'
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    messages = [
        "0|Hello",
        "1|World",
        "2|This",
        "3|Is",
        "4|A",
        "5|Test",
        "q|"
    ]

    for message in messages:
        send_data(client_socket, message)

        if message == "q|":
            print("Client is closing the connection.")
            client_socket.close()
            break

        ack = receive_ack(client_socket)
        print(f"Acknowledgment received for seq {ack}")

if __name__ == "__main__":
    client()
