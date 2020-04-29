import socket
CHUNK = 65535
port = 3000
s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #for creating socket
# socket.socket(family, type)
# AF_NET: family of ipv4 ip address
hostname = '127.0.0.1'
s.bind((hostname, port)) 
print(f"server is live on {s.getsockname()}")

while True:
	data, clientAdd = s.recvfrom(CHUNK)
	message = data.decode('ascii')
	print(f"Client: {message}")
	message_send = input("You: ")
	data = message_send.encode('ascii')
	s.sendto(data, clientAdd)