import string
import sys

#Function to decrypt the message when message and shift key are the parameters
def decrypt(message, key):
    decrypted = ""
    #Iterate through each character of the encrypted message
    for char in message:
        if char.isalpha():
            char_code = ord(char)
            char_code -= key
            if char.islower():
                if char_code < ord('a'):
                    char_code += 26
                decrypted += chr(char_code)
            else:
                if char_code < ord('A'):
                    char_code += 26
                decrypted += chr(char_code)
        else:
            #Add the non-alphabetic character to the decrypted message
            decrypted += char
    return decrypted

#function that gives the decrypted message and shift key by comparing with common english words
def decrypt_message(message):
    #List of common English words
    common_words = ["the", "and", "to", "a", "in", "that", "is", "was", "he", "for", "it", "with", "as", "his", "on", "be", "at", "by", "I", "this", "had", "not", "are", "but", "from", "or", "have", "an", "they", "which", "one", "you", "were", "her", "all", "she", "there", "would", "their", "we", "him", "been", "has", "when", "who", "will", "more", "no", "if", "out", "so", "what", "their", "up", "said", "about", "other", "into", "than", "its", "time", "only", "could", "new", "them", "man", "some", "these", "then", "two", "first", "may", "any", "like", "now", "my", "such", "over"]
    
    #Variables to hold the maximum number of common words, decrypted message and the shift key 
    max_common_words = 0
    decrypted_message = ""
    key = 0

    #Iterate in the range of 1 to 27 for each shift key
    for i in range(1,27):
        temp_decrypted = decrypt(message, i)
        common_count = 0
        for word in temp_decrypted.split():
            if word.lower() in common_words:
                common_count += 1
        if common_count > max_common_words:
            max_common_words = common_count
            decrypted_message = temp_decrypted
            key = i
    return key, decrypted_message

#Check if the encrypted message is passed as argument
if len(sys.argv) < 2:
    print("Please provide the filename of the encrypted message.")
    sys.exit()

try:
    #Open the file with encrypted message provided as command line argument
    f = open(sys.argv[1])
    encrypted_message = f.read()
    f.close()
    key, decrypted_message = decrypt_message(encrypted_message)
    #Display the shift key and the decrypted message
    print(f"Key-> {key}\nDecrypted-> {decrypted_message}")
except:
    print(f"Cannot open {sys.argv[1]}. Sorry about that.")