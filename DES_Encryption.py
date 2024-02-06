from Crypto.Cipher import DES

key = b"yonaylin"
cipher = DES.new(key, DES.MODE_ECB)

def encrypt(message):
    message = bytes(str(message), 'utf-8')
    #ensures that the message length is multiple of 8, so it pads it
    while len(message) % 8 != 0: 
        message += b"\x00"

    #Encrytion Process
    encrypted_message = cipher.encrypt(message)
    return encrypted_message

def decrypt(encrypted_message):
    #Decryption Process
    encrypted_message = cipher.decrypt(encrypted_message)
    return encrypted_message.decode().rstrip("\x00")

