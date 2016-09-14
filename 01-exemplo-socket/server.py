"""
Disciplina:	Sistemas Distribuídos
Professor:	Orlewilson B. Maia

Autor:		Orlewilson B. Maia
Data:		13/09/2016
Descrição:	Exemplo de soquete (socket) servidor 
			em Python.
Fonte:		https://shakeelosmani.wordpress.com/
			2015/04/13/python-3-socket-programming-
			example/

"""
# importa a biblioteca para trabalhar com soquete
import socket

# configurações do servidor

host = '127.0.0.1' 		# IP
port = 5005				# Porta
 
# Criando um objeto do tipo soquete (socket)
mySocket = socket.socket()

# Informa a o IP e a porta que ficará escutando
mySocket.bind((host,port))

# Adiciona um listening para escutar as solicitações
mySocket.listen(1)

# Quando chegar uma solicitação, obtém a comunicação e o endereço do cliente
conn, addr = mySocket.accept()

print ("IP do cliente conectado: " + str(addr))

while True:
	data = conn.recv(1024).decode()
	if not data: 
		break
	
	print ("Mensagem recebida do cliente: " + str(data))
             
	data = str(data).upper()
	print ("Mensagem enviada para o cliente: " + str(data))
	conn.send(data.encode())
             
conn.close()