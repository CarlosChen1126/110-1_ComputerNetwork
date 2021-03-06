# import socket module
from socket import *
import time
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a server socket
# TODO start
HOST, PORT = "127.0.0.1", 8888
serverSocket.bind((HOST, PORT))
serverSocket.listen(10)
# TODO in end
while True:
    # Establish the connection
    print('Ready to serve...')
    # TODO start
    connectionSocket, address = serverSocket.accept()
    print(str(address)+" connected")
    # TODO end
    try:
        # Receive http request from the client
        # TODO start
        message = connectionSocket.recv(1000).decode("utf-8")
        # TODO end
        print(message)
        print("======================")
        filename = message.split()[1]
        print(filename)
        f = open(filename[1:])
        # Read data from the file that the client requested
        # Split the data into lines for future transmission
        # TODO start
        outputdata = f.read()
        # TODO end
        print("outputdata:")
        print(outputdata)

        # Send one HTTP header line into socket
        # TODO start
        res = "HTTP/1.1 200 OK\r\n\r\n"
        connectionSocket.send(res.encode())
        print(len(res))
        # send HTTP status to client
        # send content type to client
        # TODO end

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode("utf-8"))
        connectionSocket.send("\r\n".encode("utf-8"))

        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        # TODO start
        res_f = "HTTP/1.1 404 Not found\r\n\r\n"
        connectionSocket.send(res_f.encode())
        # TODO end

        # Close client socket
        # TODO start
        connectionSocket.close()
        # TODO end
        print("----------------------------------------------")
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
