import socket 
import threading

#Grupo ARA (04), Judith Vilella Cantos
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
FIN = "FIN"
MAX_CONEXIONES = 2

def handle_client(conn, addr):
    print(f"[NUEVA CONEXION] {addr} connected.")

    connected = True
    while connected:
        data = []
        msg_length = conn.recv(HEADER).decode(FORMAT)
        msg_length = int(msg_length)
        data.append(conn.recv(msg_length).decode(FORMAT))
        if data[0] == 'salir':
            print("Saliendo...")
            server.close()
            conn.close()
            break
        msg_length = conn.recv(HEADER).decode(FORMAT)
        msg_length = int(msg_length)
        data.append(conn.recv(msg_length).decode(FORMAT))
        msg_length = conn.recv(HEADER).decode(FORMAT)
        msg_length = int(msg_length)
        data.append(conn.recv(msg_length).decode(FORMAT))
        if data[1] == '+':
            res = int(data[0]) + int(data[2])
            msg = "Cliente, el resultado a su operación es: " + str(res)
        elif data[1] == '-':
            res = int(data[0]) - int(data[2])
            msg = "Cliente, el resultado a su operación es: " + str(res)
        elif data[1] == '*':
            res = int(data[0]) * int(data[2])
            msg = "Cliente, el resultado a su operación es: " + str(res)
        elif data[1] == '/':
            if data[2] == '0':
                msg = "No es posible dividir por 0."
            else:
                res = int(data[0]) / int(data[2])
                msg = "Cliente, el resultado a su operación es: " + str(res)
        else:
            msg = "Operador inválido."
            print("Operador inválido.")
        msg_cliente = msg.encode(FORMAT)
        conn.send(msg_cliente)
    print("Hasta pronto.")
    conn.close()
    
        

def start():
    server.listen()
    print(f"[LISTENING] Servidor a la escucha en {SERVER}")
    CONEX_ACTIVAS = threading.active_count()-1
    print(CONEX_ACTIVAS)
    while True:
        conn, addr = server.accept()
        CONEX_ACTIVAS = threading.active_count()
        if (CONEX_ACTIVAS <= MAX_CONEXIONES): 
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
            print(f"[CONEXIONES ACTIVAS] {CONEX_ACTIVAS}")
            print("CONEXIONES RESTANTES PARA CERRAR EL SERVICIO", MAX_CONEXIONES-CONEX_ACTIVAS)
        else:
            print("OOppsss... DEMASIADAS CONEXIONES. ESPERANDO A QUE ALGUIEN SE VAYA")
            conn.send("OOppsss... DEMASIADAS CONEXIONES. Tendrás que esperar a que alguien se vaya".encode(FORMAT))
            conn.close()
            CONEX_ACTUALES = threading.active_count()-1
        

######################### MAIN ##########################


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

print("[STARTING] Servidor inicializándose...")

start()

