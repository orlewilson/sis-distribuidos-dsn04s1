"""
Disciplina:	Sistemas Distribuídos
Professor:	Orlewilson B. Maia

Autor:		Orlewilson B. Maia
Data:		13/09/2016
Descrição:	Exemplo de soquete (socket) cliente em 
			Python.
Fonte:		https://shakeelosmani.wordpress.com/
            2015/04/13/python-3-socket-programming
            -example/

"""
# importa a biblioteca para trabalhar com soquete
import socket

# configurações do servidor
host = '127.0.0.1' 		# IP
port = 5005				# Porta

# Criando um objeto do tipo soquete (socket)
mySocket = socket.socket()

# Informa a o IP e a porta que ficará escutando
mySocket.connect((host,port))
         
# Aguardando mensagem para enviar
message = input(" -> ")
         
while message != 'q':
	
	# envia a mensagem para o servidor
	mySocket.send(message.encode())
	data = mySocket.recv(1024).decode()
                 
	print ('Mensagem enviada pelo servidor: ' + data)
                 
	# Aguardando mensagem para enviar                 
	message = input(" -> ")
                 
mySocket.close()