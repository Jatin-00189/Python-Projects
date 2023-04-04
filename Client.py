import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(("127.0.0.1",4441))

while True:

    data = input("Enter here anything to send server : ")

    client.send(data.encode())

    server_data = client.recv(4096)
    if(server_data == ''): break
    if(data == 'bye'): break

    print("[+] Server sent you :  ",server_data.decode())

client.close()
print("Client Disconnected")



