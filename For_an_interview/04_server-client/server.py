import socket

USERNAME = "user"
PASSWORD = "pass"


def start_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Сервер запущен на {host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Подключаемся к {addr}")
                data = conn.recv(1024).decode('utf-8')

                username, password = data.split(',')
                if username == USERNAME and password == PASSWORD:
                    print(f"Подключено к {addr}.", end='\n\n')
                    conn.sendall('Авторизация успешна! Добро пожаловать!'.encode('utf-8'))
                else:
                    print(f"Подключение к {addr} отсутствует.", end='\n\n')
                    conn.sendall('Ошибка авторизации! Неверный логин или пароль.'.encode('utf-8'))


start_server()
