import rsa
import os

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "../platforms"

if not os.path.exists('cipher/rsa/keys'):
    os.makedirs('cipher/rsa/keys')

class RSACipher:
    def __init__(self) -> None:
        pass

    def generate_keys(self):
        (public_key, private_key) = rsa.newkeys(1024)

        with open('cipher/rsa/keys/publickey.pem', 'wb') as p:
            p.write(public_key.save_pkcs1('PEM'))

        with open('cipher/rsa/keys/privatekey.pem', 'wb') as p:
            p.write(private_key.save_pkcs1('PEM'))

    def load_keys(self):

        with open('cipher/rsa/keys/publickey.pem', 'rb') as p:
            public_key = rsa.PublicKey.load_pkcs1(p.read())   # FIX

        with open('cipher/rsa/keys/privatekey.pem', 'rb') as p:
            private_key = rsa.PrivateKey.load_pkcs1(p.read()) # FIX

        return private_key, public_key

    def encrypt(self, message, key):

        # return rsa.encrypt(mnessage.encode()('ascii'), key)
        return rsa.encrypt(message.encode('ascii'), key)  # FIX

    def decrypt(self, ciphertext, key):
        try:
            return rsa.decrypt(ciphertext, key).decode('ascii')
        except:
            return False

    def sign(self, message, key):

        # FIX: viết lại đúng hàm ký
        return rsa.sign(message.encode('ascii'), key, 'SHA-1')

    def verify(self, message, signature, key):

        try:
            rsa.verify(message.encode('ascii'), signature, key)
            return True
        except:
            return False