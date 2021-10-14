import socket

# Specify the IP addr and port number
# (use "127.0.0.1" for localhost on local machine)
# Create a socket and bind the socket to the addr
# TODO start
HOST, PORT = "127.0.0.1", 3080
# TODO end

while(True):
    # Listen for any request
    # TODO start
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    # TODO end
    print("The Grading server for HW1 is running..")

    while(True):
        # Accept a new request and admit the connection
        # TODO start
        client, address = server.accept()
        # TODO end
        print(str(address)+" connected")
        try:
            while (True):
                client.send(
                    b"Welcome to the calculator server. Input your problem ?\n")
                # Receive the data from the client and send the answer back to the client
                # Ask if the client want to terminate the process
                # Terminate the process or continue
                # TODO start
                response = client.recv(1000).decode("utf-8")
                print(response)
                answer = eval(response)
                client.send(
                    b"Receive server message:"
                )
                # need to change answer to byte
                # client.send(answer)
                print(answer)
                # TODO end
        except socket.error:
            print("except")
