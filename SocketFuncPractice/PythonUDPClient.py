import socket

target_host = "127.0.0.1"
target_port = 80

#create socket obj
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send some test data
client.sendto("BlueHat says hello python!!", (target_host, target_port))

#recieve some data
data = client.recvfrom(4096)

print data
