import socket
from threading import Thread

BYTES_TO_READ = 4096
PROXY_SERVER_HOST = 'localhost'
PROXY_SERVER_PORT = 8080

def send_request(host, port, request):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
        client_sock.connect((host,port))
        client_sock.send(request)
        client_sock.shutdown(socket.SHUT_WR)
        
        data = client_sock.recv(BYTES_TO_READ)
        result = b'' + data
        while len(data) > 0:
            data = client_sock.recv(BYTES_TO_READ)
            result += data
        
        return result
    
def handle_connection(conn, addr):
    with conn:
        print(f"Connected by {addr}")
        request = b''
        while True:
            data = conn.recv(BYTES_TO_READ)
            # If the socket is closed to writes (no more data), then break
            if not data:
                break
            print(data)
            request += data
        response = send_request("www.google.com", 80, request)
        #print(response)
        conn.sendall(response)
        
            
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        server_sock.bind((PROXY_SERVER_HOST, PROXY_SERVER_PORT))
        server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_sock.listen(2)
        conn, addr = server_sock.accept()
        handle_connection(conn, addr)
        
def start_threaded_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((PROXY_SERVER_HOST, PROXY_SERVER_PORT))
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.listen(2)
        while True:
            conn, addr = sock.accept()
            thread = Thread(target=handle_connection, args=(conn,addr))
            thread.run()
            
#start_server()
start_threaded_server()