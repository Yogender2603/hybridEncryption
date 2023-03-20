import socket
import pyaes
import blowfish
from pyDes import *




s= socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host, port))
password = (s.recv(1024).decode())
text = (s.recv(1024).decode())


l= len(text)
text1 = list(text)

text2 = []
for i in range(0, int(l/3)):
    text2.append(text1[i])
    textf= ''.join(text2)

text3 = []
for i in range(int(l/3),int(2*l/3)):
    text3.append(text1[i])
    textff= ''.join(text3)

text4=[]
for i in range(int(2*l/3),int(l)):
    text4.append(text1[i])
    textfff = ''.join(text4)


print("The part of text are:")
print(textf)
print(textff)
print(textfff,"\n\n\n")

count9=len(password)
for i in range(0, (32-count9)):
    password = password+"x"



pas = list(password)

print(pas)

k = []
count = 0
for i in pas:
    if i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9' or i == '0' :
        k.append(int(i))
        count = count+1
    if count == 3:
        break
print(k)

x1 = k[0] % 3
x2 = k[1] % 3
x3 = k[2] % 3

##-------------ENCRYPTION---------------##
print("Encryption of those part of message on the basis of keys :- ")
print("\n")
final_encrypt=[]

##--------FOR FIRST PART
##---textf--

count1 = len(textf)
if x1 == 0:
    plaintext = textf
    key = password
    key = key.encode('utf-8')
    aes = pyaes.AESModeOfOperationCTR(key)
    ciphertext = aes.encrypt(plaintext)
    print("Encrypted with AES")
    final_encrypt.append(ciphertext)
    print(ciphertext, "\n")


elif x1 == 1:

    key=bytes(password, 'utf-8')
    cipher = blowfish.Cipher(key)

    if len(textf) % 8!= 0:
        for i in range(0, 8-len(textf)%8):
            textf = textf+"#"

    plaintext = bytes(textf,'utf-8')
    ciphertext1 = cipher.encrypt_ecb(plaintext)
    encrpted_data1 = b"".join(ciphertext1)
    print("Encrypted data with BLOWFISH")
    final_encrypt.append(encrpted_data1)
    print(encrpted_data1, "\n")



elif x1 == 2:
    p1=[]
    for i in range(0, 8):
        p1.append(pas[i])

    pa1 = ''.join(p1)
    key = pa1
    key = key.encode('utf-8')
    d = des(key)

    if len(textf)%8!=0:
        for i in range(0,8-len(textf)%8):
            textf=textf+"#"

    ciphertext2=d.encrypt(textf)
    print("Encrypted with DES")
    final_encrypt.append(ciphertext2)
    print(ciphertext2, "\n")



##----------FOR SECOND PART

count2 = len(textff)

if x2 == 0:
     plaintext = textff
     key = password
     key = key.encode('utf-8')
     aes = pyaes.AESModeOfOperationCTR(key)
     ciphertext = aes.encrypt(plaintext)
     final_encrypt.append(ciphertext)
     print("Encrypted with AES")
     print(ciphertext, "\n")

elif x2 == 1:

    key=bytes(password, 'utf-8')
    cipher= blowfish.Cipher(key)
    if len(textff)%8!=0:
        for i in range(0,8-len(textff)%8):
            textff = textff + "#"

    plaintext = bytes(textff,'utf-8')
    ciphertext1 = cipher.encrypt_ecb(plaintext)
    encrpted_data2 = b"".join(ciphertext1)
    print("Encrypted with BLOWFISH")
    final_encrypt.append(encrpted_data2)
    print(encrpted_data2, "\n")

elif x2 == 2:
    p2 = []
    for i in range(0,8):
        p2.append(pas[i])

    pa2=''.join(p2)
    key = pa2
    key = key.encode('utf-8')
    d = des(key)

    if len(textff)%8!= 0:
        for i in range(0, 8-len(textff)%8):
            textff = textff+"#"

    ciphertext2= d.encrypt(textff)
    final_encrypt.append(ciphertext2)
    print("encypted with DES")
    print(ciphertext2, "\n")

## FOR THIRD PART


count3= len(textfff)

if x3 == 0:
    plaintext = textfff
    key = password
    key = key.encode('utf-8')
    aes = pyaes.AESModeOfOperationCTR(key)
    ciphertext = aes.encrypt(plaintext)
    final_encrypt.append(ciphertext)
    print("Encrypted with AES")
    print(ciphertext, "\n")

elif x3 == 1:
    key = bytes(password, 'utf-8')
    cipher = blowfish.Cipher(key)
    if len(textff)%8!= 0:
        for i in range(0,8-len(textff)%8):
            textfff = textfff+"#"

    plaintext = bytes(textfff,'utf-8')
    ciphertext1 = cipher.encrypt_ecb(plaintext)
    encrpted_data3 = b"".join(ciphertext1)
    final_encrypt.append(encrpted_data3)
    print("Encrypted with BLOWFISH")
    print(encrpted_data3, "\n")

elif x3 == 2:
    p3 = []
    for i in range(0, 8):
        p3.append(pas[i])

    pa3 = ''.join(p3)
    key = pa3
    key = key.encode('utf-8')
    d = des(key)

    if len(textfff)%8!= 0:
        for i in range(0, 8-len(textfff)%8):
            textfff = textfff+"#"

    ciphertext2 = d.encrypt(textfff)
    final_encrypt.append(ciphertext2)
    print("Encrypted with DES")
    print(ciphertext2, "\n")
    print("\n\n\n")

print("The final array containing encrypt data: ")
print(final_encrypt)
print("\n\n")


##----------FOR DECRYPTION-------------##
final_decrypt="";

#  @@ first part
if x1 == 0:
    aes = pyaes.AESModeOfOperationCTR(key)
    decryptedf = aes.decrypt(ciphertext)
    print("Decrypt with AES")
    final_decrypt = final_decrypt+str(decryptedf.decode('utf-8'))
    print(decryptedf.decode('utf-8'), "\n")
elif x1 == 1:
    print("Decrypted with BLOWFISH ")
    dec1 = (b"".join(cipher.decrypt_ecb(encrpted_data1)))
    final_decrypt = final_decrypt+dec1.decode('utf-8')
    print(dec1[0:count1].decode('utf-8'), "\n")

elif x1 == 2:
    decrypted1 = d.decrypt(ciphertext2)
    print("Decrypted with DES")
    final_decrypt = final_decrypt+str(decrypted1.decode('utf-8'))
    print(decrypted1[0:count1].decode('utf-8'), "\n")

#  @@ second part
if x2 == 0:
    aes = pyaes.AESModeOfOperationCTR(key)
    decryptedff = aes.decrypt(ciphertext)
    print("Decrypt with AES")
    final_decrypt = final_decrypt+str(decryptedff.decode('utf-8'))
    print(decryptedff.decode('utf-8'), "\n")

elif x2 == 1:
    print("Decrypted with BLOWFISH ")
    dec2 = (b"".join(cipher.decrypt_ecb(encrpted_data2)))
    final_decrypt = final_decrypt+dec2.decode('utf-8')
    print(dec2[0:count2].decode('utf-8'), "\n")

elif x2 == 2:
    decrypted2=d.decrypt(ciphertext2)
    print("Decrypted with DES")
    final_decrypt = final_decrypt+str(decrypted2.decode('utf-8'))
    print(decrypted2[0:count2].decode('utf-8'), "\n")


#   @@ third part
if x3 == 0:
    aes = pyaes.AESModeOfOperationCTR(key)
    decryptedfff = aes.decrypt(ciphertext)
    print("Decrypt with AES")
    final_decrypt = final_decrypt + str(decryptedfff.decode('utf-8'))
    print(decryptedfff.decode('utf-8'), "\n")

elif x3 == 1:
    print("Decrypted with BLOWFISH ")
    dec3 = (b"".join(cipher.decrypt_ecb(encrpted_data3)))
    final_decrypt = final_decrypt+dec3.decode('utf-8')
    print(dec3[0:count3].decode('utf-8'), "\n")

elif x3 == 2:
    decrypted3 = d.decrypt(ciphertext2)
    print("Decrypted with DES")
    final_decrypt = final_decrypt + str(decrypted3.decode('utf-8'))
    print(decrypted3[0:count3].decode('utf-8'), "\n")


s.send(bytes("thank you we have securely encrypt and decrypt your message", 'utf-8'))
s.close()
