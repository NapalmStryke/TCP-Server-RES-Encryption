
import socket as s
import DES_Encryption

def startServer():
    host = '127.0.0.1'
    port = 8888
    address = (host, port)
    serverSocket = s.socket(s.AF_INET, s.SOCK_STREAM)
    serverSocket.bind(address)
    serverSocket.listen(5)
    print("Waiting for connection....")
    
    #receives from the client the user input using receive() function
    try:
        clientSocket, address = serverSocket.accept()
        print("Client", address, "connected!")
        print("------------------------------------")
        while True:
            message = receive(clientSocket)
            print(message)
            if str(message).lower() == "shutdown" or not message:
                print("Server is shutting down.....")
                break
    except ConnectionAbortedError:
        print("Connection Aborted!")

#receives data from client user input and decodes it into string format
def receive(clientSocket):
    clientMessage = clientSocket.recv(1024)
    return clientMessage.decode() 


startServer()
