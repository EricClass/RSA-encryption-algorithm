# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 05:10:14 2019

@author: Eric
"""
"""

"""


#function to encrypt
def encrypt(message, encryption_key, n ):
    #encryption_keye is the encryption key, message is the message to be encrypted, and n = prime number p * prime number q
    #Encrypted_message is a list containing the encrypted characters
    Encrypted_message = ""
    for char in message:
        if ord(char)>=97:
            #if we have a 'a-z'
            Encrypted_message=Encrypted_message+chr(((ord(char)-97) ** encryption_key)%n)
        else:
            #for symbol character '!@#$%^&*' and upper case characters
            Encrypted_message=Encrypted_message+chr(((ord(char)) ** encryption_key) % n)
    return Encrypted_message
    


def decrypt(Encrypted_message, d, n):
    print(Encrypted_message)
    Decrypted_message=""
    #Decrypted_message is an empty string for copying every decrypted character
    for char in Encrypted_message:
        Char_ASCCI_Number=(ord(char) ** d) % n
        #every decrypted character is added to our Decrypted_message string
        if Char_ASCCI_Number <= 26:
            Char_ASCCI_Number = Char_ASCCI_Number + 97
            Decrypted_message = Decrypted_message + chr(Char_ASCCI_Number)
        else:
            Decrypted_message = Decrypted_message + chr(Char_ASCCI_Number)
    return Decrypted_message



#function to find the greated Common Divisor
def greatestCommonDivisor(e,t):
    while(encryption_key>0):
        temp = encryption_key
        encryption_key = t%e
        t = temp
    return t


#function of calculating the encryption key
def calculate_Encryption_Key( Qn ):
    for encryption_key in range(2,Qn):
        if(greatestCommonDivisor(encryption_key,Qn)==1):
            return encryption_key
    return -1


#function of calculating the decryption key
def calculate_Decryption_key( encryption_key, Qn ):
    k=1
    while(1):
        k = k + Qn
        if(k%encryption_key==0 and k/encryption_key!=encryption_key ):
            #if the decryption key is different from the encryption key we return it
            decryption_key = k/encryption_key
            return int(decryption_key)


#function for checking whether a number is a prime number
def isPrime(x):
    count = 0
    #count  is a variable for counting all factors of a number less than it, it is a prime number if it has only two factors
    for i in range(1, x+1):
        if x%i =0:
            count = count + 1
    return bool(count==2) #return a boolean answer, true if it's a prime number, and no if its not


print("Welcome to RCA program"+"\n")
#prompting the user to enter prime numbers p and q, we loop until the correct input comes
z = True
while z:
    #we loop until z becomes false, if a prime number is entered
    p = int(input('enter a large prime number p: '))
    if not isPrime(p):
        #if p is not a prime number we give the message and require another p
        print("\nWRONG INPUT (This number is not Prime. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself)\n")
    else:
        #if p is a prime number we exit the loop
        z = False
z = True
while z:
    q = int(input('enter a prime number q:'))
    if not isPrime(q):
        #if q is not a prime number we give the message and prompt another q
        print("\nWRONG INPUT (This number is not Prime. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself)\n")
    elif (p*q<130):
        #if p*q is a small number we require another p, for p*q to be greater than ascii values of characters
        print("Q(n)=p*q must be greater than 130, enter a large q")
    else:
        #if q is a prime number we exit the loop
        z = False
#if all conditions are met, we proceed with the program
if isPrime(q) and isPrime(p):
    n = p * q
    print("n = p * q  "+"\nn="+str(n))
    Qn = (p-1)*(q-1)
    print("Result of Q(n):\t = "+str(Qn))
    e = calculate_Encryption_Key( Qn )
    d = calculate_Decryption_key( e, Qn )
    print("\nRSA public key is (n = " +str(n)+", e = " +str(e) +")")
    print("RSA private key is (n = " +str(n)+ ", d = " +str(d)+ ")")
    
    msg=input("enter the message to be encrypted: ")
    encryptedText=encrypt(msg,e,n)
    print("\n"+"The encrypted message is: "+ str(encryptedText))
    decryptedText=decrypt(encryptedText, d, n)
    print("\n"+"The decrypted message is: "+ str(decryptedText))
        