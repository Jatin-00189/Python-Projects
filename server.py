import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind(("127.0.0.1",4441))

server_socket.listen(10)

print("Server is listning here 127.0.0.1:4441........")

while True:

    connection,address = server_socket.accept()

    print("[+] Got Connection from {}".format(address))

    while True:

        data = connection.recv(1024)
        if(data.decode() == 'bye'): break
        print("[+] Client says :",data.decode())
        server_data = input("Enter to send client : ")
        connection.send(server_data.encode())

    connection.close()
