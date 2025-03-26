

from flask import Flask, request, jsonify
from flask_cors import CORS

def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == "encrypt" else -shift
            ascii_offset = 65 if char.isupper() else 97
            new_char = chr((ord(char) - ascii_offset + shift_amount) % 26 + ascii_offset)
            result += new_char
        else:
            result += char
    return result

app = Flask(__name__)
CORS(app)

@app.route('/cipher', methods=['POST'])
def cipher():
    data = request.json
    text = data.get("text", "")
    shift = int(data.get("shift", 0))
    mode = data.get("mode", "encrypt")
    result = caesar_cipher(text, shift, mode)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)