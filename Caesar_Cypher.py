
#INPUT
#pInput is the users chosen phrase that they want to encrypt/decrypt
#kInput is the key, or how many letters they want to move forward in the caesar cypher
#mInput is the mode, Encryption or Decryption, E or D.
#Other Variables
#c is a counter to end while loops
#alphabet is the alphabet and alphalist is alphabet in list form

pInput = ""
kInput = int()
mInput = ""
c= int()
alphabet = 'abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ'
alphaList = list(alphabet)
#Function for pInput to make the code neater, as well as function as 1/3 of the prompt
#input: pInput
def pInputPrompt(pInput):
    print("Welcome to custom AP CSP Caesar Cyphar Multipurpose Encryption Tool. \n")
    print("Please enter the phrase you would like to encrypt or decrypt. Use the English Alphabet only.\n")
    c = 0
    while c != 1:
        pInput = str(input())
        if pInput.isalpha():
            c = 1
        else:  
            print("Please try again and ensure that your phrase is fully in English\n")  
            c = 0  
    return pInput
#Function for the kInput to make code neater, as well as function as the other 1/3 of the prompt
#input: kInput
def kInputPrompt(kInput):
    print("\nNow please enter you're desired key as a number i.e. 1\n")
    c=0
    while c!=1:
        try:
            kInput = int(input())
            kInput = int(kInput)
            kInput = kInput % len(alphaList)
            c=1
        except ValueError:
            print("Please try again")
            c=0      
    return kInput

#Function for the mInput to make the code neater, as well as function as the final 1/3 of the promp
#input: mInput
def mInputPrompt(mInput):
    print("\nNow please enter the mode; E for encryption or D for decryption\n")
    c=0
    while c!=1:
        mInput = str(input())
        if mInput == "E":
            print("\nSelected Mode: Encryption\n") 
            c=1
        elif mInput == "D":
            print("\nSelected Mode: Decryption\n")
            c=1
        else:
            print("\n INVALID MODE\n Please try again\n")
    return mInput
#Combines each of the input's functions and the cypher function to make the code more concise and end in one call.
def prompt(pInput, kInput, mInput):
    cypher(pInputPrompt(pInput), kInputPrompt(kInput), mInputPrompt(mInput))
    return pInput, kInput, mInput
#Takes all of the inputs (pInput, kInput, and mInput) to then shift the phrase b the user's desired key, wether they be encrypting or decrypting
#pList is the list form of pInput
#Crypted is the new encrypted/decrypted phrasse in list form. Which is then printed as a string under cryptedString
#output: cryptedString, see comment above
def cypher(p, k, m):
    pList = list(p)
    crypted = []
    for i in range(len(pList)):
        for j in range(len(alphaList)):
            if (pList[i] == alphaList[j]):
                if m == "D":
                    if (j - k) < 0:
                        fixed = (j - k) + len(alphaList)
                        crypted.append(alphaList[fixed])
                    else:
                        crypted.append(alphaList[j - k])
                if m == "E":
                    if (j + k) > len(alphaList):
                        fixed = (j + k) - len(alphaList)
                        crypted.append(alphaList[fixed])
                    else:
                        crypted.append(alphaList[j + k])
    cryptedString = ""
    for letter in crypted:
        cryptedString += letter
    return print("Your cyphered phrase is: " + cryptedString)

prompt(pInput, kInput, mInput)    

