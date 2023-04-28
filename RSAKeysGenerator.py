import os
from Crypto.PublicKey import RSA
from time import sleep

user = input('Generate new keys? (y/n): ')
if user == 'y':
    print('Generating...')
    key = RSA.generate(2048)
    try:
        os.mkdir('keys')
        os.mkdir('keys/foreign')
    except FileExistsError:
        pass
    with open('keys/privatekey.pem', 'wb') as f:
        print('Creating private key file...')
        f.write(key.export_key('PEM'))
    with open('keys/publickey.pem', 'wb') as f:
        print('Creating public key file...')
        f.write(key.publickey().export_key('PEM'))
    print('Done!')
    sleep(3)
else:
    print('Exiting...')
    sleep(1.5)