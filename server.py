import socket
import pickle
import getlog
HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET is address family and INET support ipv4
s.bind((socket.gethostname(), 1234)) #1234 is port number
s.listen(5)

evtLogs = getlog.get_log()
print(type(evtLogs))

while True:
    clientSocket, address = s.accept()
    print(f"Connection from {address} has been established!")

    msg = pickle.dumps(evtLogs)

    msg = bytes(f'{len(msg):<{HEADERSIZE}}',"utf-8") + msg

    clientSocket.send(msg)
    