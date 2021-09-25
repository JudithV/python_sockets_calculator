import socket
import sys

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
SALIR = "salir"
#Grupo ARA (04), Judith Vilella Cantos
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

def bienvenido():
    print("Bienvenido a su calculadora de Python. Teclee la palabra salir para cerrarla o cualquier otra para seguir.")

if  (len(sys.argv) == 3):
    SERVER = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (SERVER, PORT)
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print (f"Establecida conexión en [{ADDR}]")
    msg = ""
    while msg != SALIR :
        bienvenido()
        msg = input()
        if(msg == SALIR):
            break
        print("Operador(+ - / *): ")
        operator = input()
        print("Operando 1: ")
        operandA = input()
        print("Operando 2: ")
        operandB = input()
        send(operandA)
        send(operator)
        send(operandB)
        print("El servidor dice: ", client.recv(2048).decode(FORMAT))
        

    print("Envio al servidor: ", SALIR)
    send(SALIR)
    client.close()
else:
    print ("Oops!. Parece que algo falló. Necesito estos argumentos: <ServerIP> <Puerto>")