import socket

def http_request(method,ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip,80))
    if method == 'HEAD':
    	s.send(b'HEAD / HTTP/1.1\n\n')
    elif method == 'DELETE':
        s.send(b'DELETE / HTTP/1.1\n\n')
    elif method == 'GET':
    	s.send(b'GET / HTTP/1.1\n\n')
    elif method == 'GET3': 
    	s.send(b'GET / HTTP/3.3\n\n')
    elif method == 'JUNK':
        s.send(b'GET / JUNK/1.1\n\n')
    msg = s.recv(1024)
    s.close()
    print(msg.decode('utf-8'))
