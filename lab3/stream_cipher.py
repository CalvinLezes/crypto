from Crypto.Cipher import ARC4
from Crypto.Random import get_random_bytes

def encrypt_file(input_file, output_file, key):
    cipher = ARC4.new(key)
    with open(input_file, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            data = f_in.read()
            encrypted_data = cipher.encrypt(data)
            f_out.write(encrypted_data)

def decrypt_file(input_file, output_file, key):
    cipher = ARC4.new(key)
    with open(input_file, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            data = f_in.read()
            decrypted_data = cipher.decrypt(data)
            f_out.write(decrypted_data)

# Генерация случайного ключа длиной 16 байт
key = get_random_bytes(32)

# Шифрование файла
encrypt_file('open_text.txt', 'encrypted.txt', key)

# Расшифрование файла
decrypt_file('encrypted.txt', 'decrypted.txt', key)