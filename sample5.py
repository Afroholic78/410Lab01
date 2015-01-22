import socket
import sys
try:
	import thread
except ImportError:
	import _thread as thread

def client_thread(conn):
	while 1:
		data = conn.recv(4048)
		print (data)
		data = data[0:(len(data)-2)] + " Mickael"
		conn.sendall(data)

try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as msg:
	print("Failed to create socket")
	print("Error code: " + str(msg[0]) + ", Error message: " + msg[1])
	sys.exit()
print("socket created")

host = ""
port = 8080
try:
	s.bind((host,port))
except:
	print("Did not bind on " + host + port)
	sys.exit()

s.listen(5)

while 1:
	conn, addr = s.accept()
	thread.start_new_thread(client_thread, (conn, ))
conn.close()
s.close()