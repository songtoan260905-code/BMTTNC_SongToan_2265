from flask import Flask, request, jsonify 
from Cipher.Caesar.caesar_cipher import CaesarCipher 
from Cipher.Vigenere.vigenere_cipher import VigenereCipher 
app = Flask(__name__)

# CAESER
caeser_cipher = CaesarCipher()

@app.route("/api/caeser/encrypt", methods=['POST'])
def caeser_encrypt():
    data = request.json 
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})


@app.route("/api/caeser/decrypt", methods=['POST'])
def caeser_decrypt():
    data = request.json 
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caeser_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

# VIGENERE
vigernere_cipher = VigenereCipher

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json 
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigernere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/dencrypt', methods=['POST'])
def vigenere_dencrypt():
    data = request.json 
    cipher_text = data['cipher_text']
    key = data['key']
    dencrypted_text = vigernere_cipher.vigenere_dencrypt(cipher_text, key)
    return jsonify({'dencrypted_text': dencrypted_text})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)