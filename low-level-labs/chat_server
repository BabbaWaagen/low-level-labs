import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0",5555))
server.listen()

clients = []

def handle(client):

    while True:
        try:
            msg = client.recv(1024)
            for c in clients:
                c.send(msg)
        except:
            clients.remove(client)
            client.close()
            break

while True:

    client, addr = server.accept()
    print("Connected:",addr)

    clients.append(client)

    thread = threading.Thread(target=handle,args=(client,))
    thread.start()
