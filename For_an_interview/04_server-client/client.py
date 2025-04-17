import socket


def start_client(host='127.0.0.1', port=65432):
    username = input("Введите логин: ")
    password = input("Введите пароль: ")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall(f"{username},{password}".encode('utf-8'))

        response = client_socket.recv(1024).decode('utf-8')
        print("Ответ от сервера:", response)


start_client()
