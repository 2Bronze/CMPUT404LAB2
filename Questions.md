Question 1: First you import socket. The module is included with python since 3.11 and you intialize a socket (socket.socket(fsmily, type)), with the argument type being socket.SOCK_STREAM, which represents TCP.

Question 2: The client initilizes the connection, whereas the server listens for the connection. The client makes a request and the server responds to said request. 

Question 3: Use the line 'sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)'. We use the SO_REUSEADDR, which represents resuse address and we set it to 1. 

Question 4: We get the clients ip and port.

Question 5: Sends Null character, so client knows to close the connection.

Question 6: 