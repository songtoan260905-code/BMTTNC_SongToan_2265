from flask import Flask, request, jsonify, json
from Cipher.Caesar.caesar_cipher import CaesarCipher
from Cipher.Vigenere.vigenere_cipher import VigenereCipher
from Cipher.playfair.playfair_cipher import PlayfairCipher
from Cipher.railfence.railfence_cipher import RailFenceCipher
from Cipher.transposition.transposition_cipher import TranspositionCipher
app = Flask(__name__)

# CAESAR
caeser_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=['POST'])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caeser_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=['POST'])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caeser_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

# VIGENERE
vigernere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigernere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigernere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# RAILFENCE
railfence_cipher = RailFenceCipher()

@app.route('/api/railfence/encrypt', methods=['POST'])
def rail_fence_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])

    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)

    return jsonify({'encrypted_text': encrypted_text})


@app.route('/api/railfence/decrypt', methods=['POST'])
def rail_fence_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])

    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)

    return jsonify({'decrypted_text': decrypted_text})
# PLAYFAIR
playfair_cipher = PlayfairCipher()
@app.route('/api/playfair/creatematrix', methods=['POST'])
def create_matrix():
    data = request.json
    key = data['key']

    matrix = playfair_cipher.create_matrix(key)

    return jsonify({
        "matrix": matrix
    })
@app.route('/api/playfair/encrypt',methods=['POST'])
def playfair_encrypted():
    data = request.json
    plain_text = data['plain_text']
    key = data[key]
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
    return jsonify({"encrypted_text" : encrypted_text})
@app.route('/api/playfair/decrypt',methods=['POST'])
def playfair_decrypted():
    data = request.json
    cipher_text = data['cipher_text']
    key = data[key]
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
    return jsonify({"decrypted_text" : decrypted_text})


#TRANSPOSITION
transposition_cipher = TranspositionCipher()

@app.route('/api/transpositon/encrypt', methods=['POST'])
def transposition_encrypt():
    data = request.get-json()
    plain_text = data.get()('plain_text')
    key = int(data.get(key))
    encrypted_text = transposition_cipher.encrypt(plain_text,key)
    return jsonify({'encrypted_text':encrypted_text})

@app.route('/api/transpositon/decrypt', methods=['POST'])
def transposition_decrypt():
    data = request.get-json()
    cipher_text = data.get()('cipher_text')
    key = int(data.get(key))
    decrypted_text = transposition_cipher.decrypt(cipher_text,key)
    return jsonify({'decrypted_text':decrypted_text})



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)