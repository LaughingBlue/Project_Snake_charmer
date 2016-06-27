import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 168

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#init
server.bind((bind_ip, bind_port))

#start listening, connection limit 5
server.listen(5)

print "[*] Listening on %s:%d" % (bind_ip, bind_port)

#client process thread
def handle_client(client_socket):
    #display data sent from client
    request = client_socket.recv(1024)

    print "[*] Received: %s" % request

    #return a packet
    client_socket.send("ACK!")
    client_socket.close()

while True:
    client,addr = server.accept()

    print "[*] Accepted connection from: %s:%d" % (addr[0],addr[1])

    #data from client thread
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()


