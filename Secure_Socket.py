

import socket
#importing regex
import re
#importing SSL
import ssl


#Creating a Socket object 
try :
	Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except Exception as er:
	print(str(er))
	quit()


#Taking Http URL from user
URL = input('Enter http url path of your text file\n')
if URL.startswith('https://'):
	Host = re.findall('https://(\S+)/', URL)
	print(Host)
	Hostname = Host[0]
	Port = 443
	#if its a https url context and wrap will be created
	My_Context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
	#wrapped socket in context 
	My_Sock = My_Context.wrap_socket(Sock, server_side = False, server_hostname = Hostname )

else :
	Host = re.findall('http://(\S+)/', URL)
	print(Host)
	Hostname = Host[0]
	Port = 80
	My_Sock = Sock


#Creating a Socket connection 
try :
	My_Sock.connect((Hostname,Port))
	print('Connected Succesfully\n')
except Exception as er:
	print(str(er))
	print('Connection Failed\n')
	quit()

#Getiing Directory from user to save file
User_File = input('Kindly Enter Directory to store file\n')
File_Name = f'{User_File.strip()}/{Hostname.strip()}.txt'
print('Writing to',File_Name,'\n')

#Creating GET request command 
try :
	cmd = f'GET {URL} HTTP/1.0\r\n\r\n'.encode() #By Deafult encodes to "UTF-8"
except Exception as er:
	print(str(er))
	print('GET Command Failed\n')
	quit()

#Sending the request to Host
My_Sock.send(cmd)

#writing to file
file = open(File_Name,'w+')

#receiving response untill its empty 
while True:
	try :
		message = My_Sock.recv(1024).decode()
	except Exception as er:
		print(str(er))
		print('Cannot receive message\n')
		quit()

	if len(message)<1:
		print('----------------------------------------------EOL----------------------------------------------------')
		break
	try:
		file.write(message)
	except:
		pass

print('Data fetched Succesfully\n')
My_Sock.close()



