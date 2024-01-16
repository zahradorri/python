Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def encrypt(text, key):
...     encrypted_text = ""
...     for char in text:
...         encrypted_text += chr((ord(char) + key) % 128)
...     return encrypted_text
... 
... def decrypt(encrypted_text, key):
...     decrypted_text = ""
...     for char in encrypted_text:
...         decrypted_text += chr((ord(char) - key) % 128)
...     return decrypted_text
... 
... message = "Hello, World!"
... encryption_key = 3
... encrypted_message = encrypt(message, encryption_key)
... print("Encrypted Message:", encrypted_message)
