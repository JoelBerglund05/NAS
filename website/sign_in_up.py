import bcrypt
import base64
from Crypto.Cipher import AES
from Crypto import Random
import os
import os.path
from os.path import isfile, join
from os import listdir
import secrets

class Hash:
    def check_hash(password, hashed_password):
        return bcrypt.checkpw(password.encode("UTF-8"), hashed_password)

    def get_hash(password, salt):
        return bcrypt.hashpw(password.encode("UTF-8"), bcrypt.gensalt(salt))
    

class Encryptor:
    def __init__(self, key):
        self.key = key

    def gen_key():
        key = secrets.token_bytes(32)
        return key


    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)
    
    def encrypt(self, message, key, key_size=256):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)
    
    def encrypt_file(self, filename):
        with open(filename, "rb") as file:
            plaintext = file.read()
        enc = self.encrypt(plaintext, self.key)
        with open(filename, + ".enc", "wb") as file:
            file.write(enc)
        os.remove(filename)
            
    def decrypt(self, cipherText, key):
        iv = cipherText[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(cipherText[AES.block_size:])
        return plaintext.rstrip(b"\0")
    def decrypt_file(self, filename):
        with open(filename, "rb") as file:
            ciphertext = file.read()
        dec = self.decrypt(ciphertext, self.key)
        with open(filename[:-4], "wb") as file:
            file.write(dec)
        os.remove(filename)

    def get_all_files(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dirs = []
        for dir_name, subdir_list, file_list in os.walk(dir_path):
            for file_name in file_list:
                if file_name.endswith(".enc"):
                    dirs.append(dir_name + "\\" + file_name)
        return dirs
    
    def encrypt_all_files(self):
        dirs = self.get_all_files()
        for file_name in dirs:
            self.encrypt_file(file_name)
    
    def decrypt_all_files(self):
        dirs = self.get_all_files()
        for file_name in dirs:
            self.decrypt_file(file_name)