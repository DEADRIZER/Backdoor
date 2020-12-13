import socket

def aware():
	"""Main fonction"""
	s= socket.socket()

	# On définit notre host / port 
	host= socket.gethostname() # Get the host name
	port= 8080
	print(f"#{host} listening on :{port}")

	while True:	

def sendOrder():
	Orders= {
		1: "Keylogger",
		2: "Exit",
	}


if __name__ == '__main__':
	aware()