import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

print('Welcome to RSA Encryptor')
def main():
    user = input('What you want to do?\n[1] - Encrypt\n[2] - Decrypt\n')
    if user == '1':
        rsaencrypt()
    elif user == '2':
        rsadecrypt()
    else:
        print(f'ERROR: {user} - Incorrect argument')

def rsaencrypt():
    print("WARNING: Check that the 'publickey.pem' file is in the 'keys/foreign' folders, otherwise an error may occur.")
    input('Press anything to continue...')
    try:
        with open('keys/foreign/publickey.pem', 'rb') as f:
            key = RSA.importKey(f.read())
    except FileNotFoundError:
        print("ERROR: The 'publickey.pem' file appears to be missing from the 'keys/foreign' folder.\nWithout it you will not be able to encrypt the message!\nAsk your conversation partner to send you a 'publickey.pem'")
        return
    key = PKCS1_OAEP.new(key)
    msg = str.encode(input('What message do you want to encrypt?\n'))
    enc_msg = key.encrypt(msg)
    enc_msg = base64.b64encode(enc_msg)
    enc_msg = enc_msg.decode('utf-8')
    print(f'Your encrypted message:\n----------\n{enc_msg}\n----------')
    
def rsadecrypt():
    print("WARNING: Check that the 'privatekey.pem' file is in the 'keys' folders, otherwise an error may occur.")
    input('Press anything to continue...')
    try:
        with open('keys/privatekey.pem', 'rb') as f:
            key = RSA.importKey(f.read())
    except FileNotFoundError:
        print("ERROR: The 'privatekey.pem' file appears to be missing from the 'keys' folder.\nWithout it you will not be able to decrypt the message!\nCreate a new one using 'RSAKeysGenerator.py' and send 'publickey.pem' to your conversation partner")
        return
    key = PKCS1_OAEP.new(key)
    msg = input('What message do you want to decrypt?\n')
    try:
        msg = base64.b64decode(msg)
        dec_msg = key.decrypt(msg)
    except:
        print('ERROR: Something went wrong. Perhaps there is something wrong with the encrypted message?')
        return
    dec_msg = dec_msg.decode('utf-8')
    print(f'Your decrypted message:\n----------\n{dec_msg}\n----------')

main()
while True:
    user = input('Do you want to go back to the main menu? (y/n): ')
    if user == 'y':
        main()
    else:
        break