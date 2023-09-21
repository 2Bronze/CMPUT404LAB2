import socket

BYTES_TO_READ = 4096

def get(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host,port))
        sock.send(b'GET / HTTP/1.1\nHost: www.google.com\n\n')
        sock.shutdown(socket.SHUT_WR)
        chunk = sock.recv(BYTES_TO_READ)
        result = b'' + chunk
        
        while len(chunk) > 0:
            chunk = sock.recv(BYTES_TO_READ)
            result += chunk
        # Empty bytestring is sent
        sock.close()
        return result

print(get('localhost', 8080))
    