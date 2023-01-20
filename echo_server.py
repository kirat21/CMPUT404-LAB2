import socket
from threading import Thread

BYTES_TO_READ = 4096
HOST = "127.0.0.1"
PORT = 8080

def handle_connection(conn, addr):
    with conn:
        print(f"Connected by: {addr}")
        while(1):
            data = conn.recv(BYTES_TO_READ)
            if not data:
                break
            print(data)
            conn.sendall(data)

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #let us reuse the socket

        s.listen()

        conn, addr = s.accept()
        handle_connection(conn, addr)

def start_mutithreaded_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.listen(2)
        while(1):
            conn, addr = s.accept()
            thread = Thread(target=handle_connection, args=(conn, addr))
            thread.run()

    
start_server()
# #start_threaded_server()


# echo "Foobar" | nc localhost 8080 -q 1

# ://github.com/aianta/cmput404-tcp-lab
