import socket


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=socket.gethostname()

port=12345

s.bind((host,port))
s.listen(5)

print("HELLO")
x=input("Enter the user id: ")
y=input("Enter the password of 10 digit must include 3 digit: ")
z=input("Enter the message: ")

while True:
    c,addr=s.accept()

    print("get the connection from",addr)

    e=str(y)

    c.send(e.encode())
    c.send(z.encode())
    print(c.recv(1024).decode())
    c.close()