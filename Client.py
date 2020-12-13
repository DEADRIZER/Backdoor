import socket
def active():
	"""Main fonction"""

	# Get the host name
	host= socket.gethostname() 
	port= 8080
	CONN= socket.socket() 	
	CONN.connect((host, port))



if __name__ == '__main__':
	active()