import os

try:
    import socketserver
except ImportError:
    import SocketServer as socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        #print "{} wrote:".format(self.client_address[0])
        print ("ClientIP:", self.client_address[0])
        print ("Rx: ", self.data)
        # just send back the same data, but upper-cased
        #self.request.sendall(self.data.upper())
        s = "Usuario Ejemplo,99,1:40pm,Nov 2nd,2014"
        print ("Tx: ", s)
        self.request.sendall(s.encode("utf-8"))

if __name__ == "__main__":
    HOST = os.getenv("TCP_SERVER_HOST", "127.0.0.1")
    PORT = int(os.getenv("TCP_SERVER_PORT", "9999"))

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    print()
    print ("Started: %s   Port: %d" % ( HOST, PORT ))
    print ("Server: ", server)
    print

    server.serve_forever()
