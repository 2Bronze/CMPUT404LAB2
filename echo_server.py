import socket
from threading import Thread

BYTES_TO_READ = 4096
HOST = "localhost"
PORT = 8080

def handle_connection(conn, addr):
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(BYTES_TO_READ)
            # If the socket is closed to writes (no more data), then break
            if not data:
                break
            print(data)
            conn.sendall(data)
            
def start_server():    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST,PORT))
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.listen()
        conn, addr = sock.accept()
        handle_connection(conn, addr)
        
def start_threaded_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.listen(2)
        while True:
            conn, addr = sock.accept()
            thread = Thread(target=handle_connection, args=(conn,addr))
            thread.run()
    
#start_server()
start_threaded_server()