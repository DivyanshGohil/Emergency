import socket
import pickle

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET is address family and INET support ipv4
s.connect((socket.gethostname(), 1234))


while True:
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(16) #16 is buffer size
        if new_msg:
            print(f"new message length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg

        if len(full_msg) - HEADERSIZE == msglen:
            print("Full Message Recevied")

            d = pickle.loads(full_msg[HEADERSIZE:])
            print(d)

            new_msg = True
            full_msg = b''

    print(full_msg) 