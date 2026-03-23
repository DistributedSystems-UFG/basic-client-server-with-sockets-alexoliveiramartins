from socket  import *
from constCS import * #-

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # connect to server (block until accepted)

print("Escolha uma operação: ")
operation = input("[0] Adicao | [1] Subtracao | [2] Mutiplicar: ")
op1 = input("Digite o primeiro numero: ")
op2 = input("Digite o segund numero: ")

s.send(f"[{operation},{op1},{op2}]".encode())  # send some data
print("Sent operation 0, and operands 1,2 to server")
data = s.recv(1024)     # receive the response
print ("Resultado recebido do servidor: " + bytes.decode(data))            # print the result
s.close()               # close the connection
