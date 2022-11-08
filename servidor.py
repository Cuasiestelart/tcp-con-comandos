#servidor
import socket
import os
import platform
import time
host = "localhost"
port = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen(1)
print("servidor en espera de conexiones nuevas")
active, addr = server.accept()

while True:
    recibido = active.recv(1024).decode(encoding="ascii", errors="ignore")
    print("cliente: ", recibido)

    if(recibido == "salir"):

        break

    else:

        #comando os para enviar
        if(recibido == "os"):

            enviar=str(platform.system()) +" "+ str(platform.release())
            active.send(enviar.encode(encoding="ascii", errors="ignore"))

        #comando de fecha
        if(recibido == "date"):
            enviar=time.ctime()
            active.send(enviar.encode(encoding="ascii", errors="ignore"))


        #comando para directorio
        if(recibido == "ls"):
            enviar=str(os.listdir())
            active.send(enviar.encode(encoding="ascii", errors="ignore"))



active.close()
