# PyTEA
A simple Tiny Encryption Algorithm(TEA) implementation for Python3

## Usage
```py
from pytea import TEA
from binascii import b2a_hex
import os

data = b'https://github.com/bluesadi/PyTEA'
# Generate random key
# Length of key must be 16
key = os.urandom(16)
tea = TEA(key)
# Encrpytion
enc = tea.Encrypt(data)
print(b2a_hex(enc))
# Decryption
dec = tea.Decrypt(enc)
print(dec)
```