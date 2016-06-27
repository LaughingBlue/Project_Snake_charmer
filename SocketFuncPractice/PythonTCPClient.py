import socket

target_host = "127.0.0.1"
target_port = 168

#create socket obj
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#client connect
client.connect((target_host, target_port))

#send some test data
#client.send("GET / HTTP/1.1\r\nHOST: google.com\r\n\r\n")
client.send("BlueHat says hello python!!")

#recieve some data
response = client.recv(4096)

print response
