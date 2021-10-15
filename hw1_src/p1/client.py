import socket

ClientMessage = "hello"
HOST, PORT = "127.0.0.1", 3080
#HOST, PORT = "140.112.42.108", 7777
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
while(True):
    response = input(client.recv(1000).decode("utf-8")).encode("utf-8")
    client.send(response)
    response2 = input(client.recv(1000).decode("utf-8")).encode("utf-8")
    client.send(response2)
