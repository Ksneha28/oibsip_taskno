import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s_address = ("localhost", 9999)
s.bind(s_address)

# Listen for incomming connections 
s.listen(1)
print("Server listening on {}:{}".format(*s_address))

# waiting for connections
c , c_addr = s.accept()
print("connection fraom", c_addr)

# recived date from client
message = c.recv(1024)
print("recieved:", message.decode())

reply = "hi {}! I received your message.".format(c_addr)
c.send(reply.encode())

# close
c.close()
s.close()

