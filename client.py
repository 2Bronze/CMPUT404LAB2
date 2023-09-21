import socket

BYTES_TO_READ = 4096

def get(host, port):
    # AF_INET -> IPV4, SOCK_STREAM -> TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    sock.send(b'GET / HTTP/1.1\nHost: ' + host.encode('utf-8') + b"\n\n")
    sock.shutdown(socket.SHUT_WR)
    result = sock.recv(BYTES_TO_READ)
    while(len(result)>0):
        print(result)
        result = sock.recv(BYTES_TO_READ)
        
    sock.close()
 
#get('www.google.com', 80)   
get('localhost', 8080)