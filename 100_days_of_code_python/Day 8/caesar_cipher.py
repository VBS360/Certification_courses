alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
    
def encrypt(text,shift):
    cipher_text = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position+shift)%26
            new_char = alphabet[new_position]
            cipher_text+= new_char
        else:
            cipher_text += letter
    
    print(cipher_text)
    
    cont = int(input("press 0 to stop the encryption & press 1 to continue the encryption\n"))
    if cont == 1:    
        return encrypt(text,shift)        
    else:
        print("Thanks Visit Again!")
    
def decrypt(text,shift):
    cipher_text = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - shift) % 26
            new_char = alphabet[new_position]
            cipher_text += new_char
        else:
            cipher_text += letter
    print(cipher_text)
    
    cont = int(input("press 0 to stop the decryption & press 1 to continue the decryption\n"))
    if cont == 1:    
        return decrypt(text,shift)        
    else:
        print("Thanks Visit Again!")

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
    #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
    
if direction == "encode":
    encrypt(text,shift)
elif direction == "decode":
    decrypt(text,shift)
else:
    print("enter proper value for direction.")
