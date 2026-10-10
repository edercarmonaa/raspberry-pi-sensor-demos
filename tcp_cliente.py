import socket
import sys
import os

HOST = os.getenv("TCP_SERVER_HOST", "127.0.0.1")
PORT = int(os.getenv("TCP_SERVER_PORT", "9999"))

data = " ".join(sys.argv[1:])
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect((HOST, PORT))
    sock.sendall((data + "\n").encode("utf-8"))
    received = sock.recv(1024)
finally:
    sock.close()
print ("Sent:     {}".format(data))
print ("Received: {}".format(received))
