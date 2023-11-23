# Updated server.py

import socket


def receive_data(conn):
    data = conn.recv(1024).decode()
    return data


def send_ack(conn, ack):
    conn.send(ack.encode())


def server():
    server_ip = '127.0.0.1'
    server_port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(1)

    print("Waiting for a connection...")
    conn, addr = server_socket.accept()
    print(f"Connection established with {addr}")

    expected_seq = 0

    while True:
        data = receive_data(conn)

        if data == "q":
            print("Client has closed the connection.")
            conn.close()
            break

        seq_number, message = data.split('|', 1)

        # Check if the received data is the termination signal
        if seq_number == 'q':
            print("Client has closed the connection.")
            conn.close()
            break

        try:
            seq_number = int(seq_number)
            if seq_number == expected_seq:
                print(f"Received packet with seq {seq_number}: {message}")
                send_ack(conn, str(seq_number))
                expected_seq += 1
            else:
                print(f"Discarding out-of-order packet with seq {seq_number}")
        except ValueError:
            print(f"Invalid sequence number: {seq_number}")


if __name__ == "__main__":
    server()
