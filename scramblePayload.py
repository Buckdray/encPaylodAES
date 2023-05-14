from Crypto.Cipher import AES
import hashlib

def encrypt_file(input_filename, output_file, key, iv):
    key = hashlib.sha256(key.encode()).digest()

    iv = iv[:16].encode().ljust(16,b'\x00')


    print("New key:",key)
    cipher = AES.new(key,AES.MODE_CBC, iv)

    with open(input_file, 'rb') as file:
        plaintext = file.read()

    #pad the plaintext to a multiple of 16 bytes 
    print('original text:', plaintext)
    padded_plaintext = pad(plaintext)
    print('padded:',padded_plaintext)

    #Encrypt the the plaintext
    ciphertext = cipher.encrypt(padded_plaintext)   
    print('encrypted:',ciphertext)

    with open(output_file, 'wb') as file: 
        file.write(iv)
        file.write(ciphertext)

def pad(data):
    padding_len = 16 - (len(data)% 16)
    print(padding_len)
    padding = bytes([padding_len]*padding_len)
    

    #for byte_value in padding:
    #    print(byte_value)
    return data+padding



key = '3uGnMY*4UU/Dh8WZ_@@fM&/,7kv(vvKy' #has to be a 32 bytes string for 256 bit key
iv = "vw{u_%&-rJ%B@-D8"  #has to be a 16 bytes string for the IV 
input_file = "cool.txt"
output_file = "encrypted.bin"
#print(key)
#print(iv)
encrypt_file(input_file, output_file, key, iv)