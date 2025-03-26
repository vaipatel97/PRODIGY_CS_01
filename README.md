# Caesar Cipher Tool

A simple Python-based tool to encrypt and decrypt text using the Caesar cipher algorithm.

## 📜 About
The Caesar cipher is a substitution cipher where each letter in the plaintext is shifted by a fixed number of positions in the alphabet. This tool allows you to encrypt and decrypt messages easily.

## 🚀 Features
- Encrypt text using a shift value
- Decrypt text with a known shift value
- Supports uppercase and lowercase letters
- Ignores non-alphabetic characters

## 🔧 Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/caesar-cipher-tool.git
   cd caesar-cipher-tool
   ```
2. Ensure you have Python installed (version 3.x recommended).

## 🛠 Usage
Run the script using Python:
```sh
python caesar_cipher.py
```

### Example
#### Encryption:
```python
Enter text: Hello World
Enter shift value: 3
Encrypted text: Khoor Zruog
```

#### Decryption:
```python
Enter text: Khoor Zruog
Enter shift value: 3
Decrypted text: Hello World
```

## 📌 How It Works
1. Each letter is shifted forward (for encryption) or backward (for decryption) by the specified shift value.
2. Non-alphabetic characters remain unchanged.
3. The alphabet wraps around (e.g., 'Z' shifted forward by 1 becomes 'A').

## 🛡 Security Considerations
- The Caesar cipher is not secure for modern encryption needs.
- It can be easily broken using frequency analysis or brute force attacks.
- Suitable for learning cryptography basics but not for protecting sensitive data.

## 🤝 Contributing
Feel free to fork this repository and submit pull requests to improve the tool!

## 📜 License
This project is licensed under the MIT License.

## 📬 Contact
For questions or suggestions, reach out at [your-email@example.com].

---
⭐ Don't forget to give a star if you like this project!

