HYBRID ENCRYPTION:-

Safety has become a very important part of modern life. Data security is the most mandatory security of all. The data on our system is exposed to high potential risks. Due to different safety reasons we use different methods. . While most web- based applications require data security we need to focus on developing better algorithms for the purpose of encryption of the data to make it moresecure. Our aim in this project is to develop a design and implementation of a much simplified and efficient hybrid algorithm based on the Data Encryption Standard (DES),AES and blowfish algorithm which is very similar, but works on in a different way. Our Hybrid algorithm will provide more security to the storage systems.

1. METHODOLOGY:-
As we discussed above that data security is very important and the current algorithms can be under attack and data can be decrypted by the attacker for malicious use.Thus we have presented our hybrid algorithm which will be much more secured as well as perform better than the current in use algorithms.Instead of using one single algorithm to protect user’s data we have proposed a hybrid encryption system in which we will be using the three most popular encrypting algorithms:
1.DES (Data Encryption Standard)
2.AES (Advanced Encryption Standard)
3.Blowfish Algorithm
![Screenshot (137)](https://user-images.githubusercontent.com/128420302/226458582-67332d40-76c1-4252-8fd8-608c0e7be6cd.png)
Our methodology will ensure maximum data security as our algorithm will first divide the user’s message into 3 parts and use 3 different algorithms over that data. Thus the encrypting scheme will be assigned on a random basis to the parts of the message. Thus it will be very hard for an attacker to steal original data when we are using 3 different algorithms on random basis.

2. STEPS INVOLVED IN THE ALGORITHM
Client.py

1. Create a tcp/ip socket using socket.socket()
2. Enter socket parameters such that it will be a ipv4 and tcp socket,
3. Select any port number
4. Bind the socket to that port and set incoming connections you want to listen.
5. Take input from user – Username, Password, Message.
6. Take a while loop and start accepting connection From the server using socket.accept().
7. After this connection we can send the input given by the user to the server for encryption process.

Hybrid_encryption1.py

Here now we also need to connect this server with the client to receive the data he has entered and wants to be encrypted and then stored.
1. Connect the server at the same port as of client.
2. Receive the data sent to server in the same order as sent by the client on this port.
3. Store the user’s password in a variable.
4. Store the user’s message in another variable.
5.Use a for loop to detect the 3 digits in the user’s password and do (digit % 3).
6. Store the above result in an array of integers.
7. Now split the user’s message into 3 parts and store them in a list of strings.
8. Loop through the list to take string one by one and based on values in password array assign algorithm for encryption.
9. If modulo with 3 value = 0 in array assign AES algorithm to that part of text.
10. If modulo with 3 value = 1 in array assign Blowfish algorithm to that part of text.
11. If modulo with 3 value = 2 in array assign the Blowfish algorithm to that part of text.
12. Encrypt the data using the above algorithms and generate the cipher text.
13. Display the encrypted cipher text by the different algorithms.
14 Similarly as above based on the modulo 3 values decrypt the part of text using different algorithms.
15.Finally display the decrypted text and compare with the original text

3. WORKING OF THE ALGORITHM
Executing Client.py (take user's input message)
![Screenshot (128)](https://user-images.githubusercontent.com/128420302/226459935-bcb650ed-f54f-492a-af32-3bc2c0564b44.png)

Executing server.py - (encryption and decryption)
![Screenshot (157)](https://user-images.githubusercontent.com/128420302/226460520-615c1d63-84b3-44b4-a188-e3f2608e6dd4.png)

![Screenshot (158)](https://user-images.githubusercontent.com/128420302/226460695-79bfe0d5-4717-4b17-810d-3d96d3dabfb0.png)


4. Result and Conclusion:-
We have studied that our proposed hybrid algorithm for data encryption performs better than presently used encryption algorithms. We have also compared our methodology with Data Encryption Standard algorithm (DES), Data encryption standard and Advance encryption standard algorithm. We have found that our algorithm is efficient in terms of providing more security as our algorithm not allows attacker to easily decrypt the messages. It will be hard for the attacker to find the encryption algorithm as we have not used just a single encryption method. Also even if the attacker finds the 3 algorithms we have used,still oursystemwill be secured because of the randomness on the use of algorithm on different part of the message. Thus providing one more layer of security.
