import socket

HEADER = 64
PORT = 5050
SERVER = "172.18.48.1"
ADDR= (SERVER, PORT) # we use this tuple to bind to the socket (connect with the socket we are going to create)
FORMAT ='utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message=msg.encode(FORMAT)
    msg_length= len(message)
    send_length = str(msg_length).encode(FORMAT) # REMEMBER FIRST TIME WE MAKE A CONNECTION WE HAVE TO SEND
    send_length+=b' '*(HEADER-len(send_length))  # A MSG 64-BYTES LONG(HEADER msg) THAT IS THE PROTOCOL WE HAVE SET
    client.send(send_length)
    client.send(message)
    response=client.recv(3000).decode(FORMAT)   # WE ARE ASSUMING THAT MSG FROM SERVER WONT EXCEED 3000 BYTES
    print(f"[RESPONSE FROM SERVER]{response}")

while True:
    send(input("enter message for server ->"))
    
