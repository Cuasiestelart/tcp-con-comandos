import socket
host = "localhost"
port = 8080
# crear objeto llamado socket1#
socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#recibe una tupla del host y el puerto
socket1.connect((host,port))
print("inicializando cliente")

while True:
    enviar = input("Cliente: ")

    socket1.send(enviar.encode(encoding="ascii", errors="ignore"))


    recibido = socket1.recv(1024)

    print("servidor: ", recibido.decode(encoding="ascii", errors="ignore"))

socket1.close()
