#   Steps
#   1. Step -- Build the encryption function with inputs
#   2. Step -- Build the decryption function with inputs
#   3. Step -- Build body of the program to get inputs and call functions
#   4. Step -- get all the variables and lists defined


#   -- Variables --
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','!','@','#','$','%','^','&','*','(',')','_','-','+','=','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',]
message = ""
encryption_level = 0
encryption_key = 0
message_list = list(message)
encrypted_message_list = []
encrypted_index_list = []
decrypted_index_list = []
decrypted_message_list = []
encrypted_message = "".join(encrypted_message_list)
decrypted_message = "".join(decrypted_message_list)
submit = ""


 #  -- Step 1 Encryption Function --

def encryption(message,encryption_level):
    message_list = list(message)
    for letter in message_list:
        if letter in alphabet:
            encrypted_index_list.append(alphabet.index(letter) + encryption_level)
        
    for index in encrypted_index_list:
        encrypted_message_list.append(alphabet[index])
    #print(encrypted_message_list)
    encrypted_message = "".join(str(encrypted_message_list) for encrypted_message_list in encrypted_message_list)
    print(f"""This is your encrypted message:\n 
          {encrypted_message}
---------------------------------------------------------------------------------------------""")   

#  -- Step 2 Decryption Function --

def decryption(encryption_key):
    for letter in encrypted_message_list:
        if letter in alphabet:
            decrypted_index_list.append(alphabet.index(letter) - encryption_key) 

    for index in decrypted_index_list:
        decrypted_message_list.append(alphabet[index])
    #print(decrypted_message_list)
    decrypted_message = "".join(str(decrypted_message_list) for decrypted_message_list in decrypted_message_list)
    print(f"""This is your decrypted message:\n
          {decrypted_message}
---------------------------------------------------------------------------------------------""")


#  -- Step 3 Main Program --
print("""    ------------------------------------------------
    You have successfully entered the Cipher program
    ------------------------------------------------\n""")
while submit != "exit":
    submit = input("Do you want to encrypt or decrypt your message or exit the program?\n:\t").lower()


    if submit == "encrypt":
        message = input("Write your message in one line\n:\t")
        encryption_level = int(input("Write the level of encryption for your message from 1 to 5\n:\t"))
        encryption(message=message,encryption_level=encryption_level)

    if submit == "decrypt":
        if message == "":
            print("Yo do not have any message to decrypt\n")
        else:    
            encryption_key = int(input("Write the level of decryption for your message from 1 to 5\n:\t"))
            decryption(encryption_key=encryption_key)

            if encryption_key == encryption_level:
                print("Your message was succesfully decrypted\n")
            else:
                print("\nYou entered a wrong level of decryption,program will exit for security reasons")
                submit = "exit"

print("\nprogram finished")