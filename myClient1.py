import socket as s
import DES_Encryption

clientSocket = s.socket(s.AF_INET, s.SOCK_STREAM)
host = '127.0.0.1'
port = 8888
address = (host, port)
clientSocket.connect(address)

#Function to check what kind of connection is being used
def isSecure():
    print("Enter anything for non-secure connection. Enter 1 for secure connection.")
    secure = int(input("Enter Connection Type: "))
    return secure == 1

#Encodes the message & sends to server, when typed shutdown, or when the enter key is hit, the server shuts down
def send():
    while True:
        secure = isSecure()
        message = str(input("Enter Message: "))
        if message.lower() == "shutdown" or not message:
            break
        if secure:
            encrypted_message = DES_Encryption.encrypt(message.encode())
            clientSocket.sendall(str(encrypted_message).encode())
        else:
            clientSocket.sendall(message.encode())

#Entry Point    
print("Enter 0 for non-secure connection type. 1 for secure connection type.")
def main():
    send()

main()
