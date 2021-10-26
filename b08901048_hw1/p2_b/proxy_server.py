from socket import *
import sys

if len(sys.argv) <= 1:
    print(
        'Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
    sys.exit(2)

# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
# TODO start.
HOST, PORT = sys.argv[1], 7777
tcpSerSock.bind((HOST, PORT))
tcpSerSock.listen(1)
# TODO end.
while 1:
    # Strat receiving data from the client
    print('Ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from:', addr)

    # Receive request from the client
    # TODO start.
    message = tcpCliSock.recv(1000).decode()
    # TODO end.
    print(message)

    # Extract the filename from the given message
    print(message.split()[1])
    filename = message.split()[1].partition("/")[2]
    print(filename)
    fileExist = "false"
    filetouse = "/" + filename
    print(filetouse)
    try:
        # Check whether the file exist in the cache
        f = open(filetouse[1:], "r")
        outputdata = f.read()
        print("outputdata exist")
        fileExist = "true"

        # ProxyServer finds a cache hit and generates a response message
        # Send the file data to the client
        # TODO start.
        for i in range(0, len(outputdata)):
            tcpCliSock.send(outputdata[i].encode("utf-8"))
        tcpCliSock.send("\r\n".encode("utf-8"))
        # TODO end.

        print('Read from cache')
    # Error handling for file not found in cache
    except IOError:
        if fileExist == "false":
            # Create a socket on the proxyserver
            # TODO start
            sock = socket(AF_INET, SOCK_STREAM)
            HOSTW, PORTW = "127.0.0.1", 888
            # TODO end
            hostn = filename.replace("www.", "", 1)
            try:
                # Connect to the socket to webserver port
                # TODO start.
                sock.connect((HOSTW, PORTW))
                # TODO end.

                # Create a temporary file on this socket and ask webserver port for the file requested by the client
                fileobj = sock.makefile('rw', None)
                fileobj.write("GET " + filetouse + " HTTP/1.0\n\n")
                fileobj.flush()

                # Read the response into buffer
                # TODO start.
                resintobuffer = fileobj.read()
                # TODO end.

                # Create a new file in the cache for the requested file.
                # Also send the response in the buffer to client socket and the corresponding file in the cache
                # TODO start.
                buffer = resintobuffer.split("\n")
                print(buffer[0])
                if "404" in buffer[0]:
                    print("fault")
                    tcpCliSock.send(b"HTTP/1.1 404 Not found\r\n\r\n")
                    tcpCliSock.close()
                else:
                    tmpFile = open(filename, "w")
                    for item in resintobuffer:
                        tmpFile.write(item)
                    tmpFile.close()
                    tmpFileR = open(filename, "r")
                    out = tmpFileR.read()
                    out = out.split("\n")
                    res = "HTTP/1.1 200 OK\r\n\r\n"
                    tcpCliSock.send(res.encode())
                    for i in range(3, len(out)):
                        tcpCliSock.send(out[i].encode("utf-8"))
                    tcpCliSock.send("\r\n".encode("utf-8"))
                # TODO end.
            except:
                print("Illegal request")
        # else:
        #     # HTTP response message for file not found
        #     # TODO start.
        #     res_f = "HTTP/1.1 404 Not found\r\n\r\n"
        #     tcpCliSock.send(res_f.encode())
        #     # TODO end.
        #     # Close the client sockets
        #     tcpCliSock.close()
        #     # Close the server socket
        #     print("false")
        #     # TODO start.
        #     sock.close()
        #     tcpSerSock.close()
        #     # TODO end.
