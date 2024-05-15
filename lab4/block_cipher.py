from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def pad(data):
    """
    Pad the data to be a multiple of 16 bytes.
    """
    padding_length = 16 - (len(data) % 16)
    padding = bytes([padding_length]) * padding_length
    return data + padding

def unpad(data):
    """
    Remove the padding from the data.
    """
    padding_length = data[-1]
    return data[:-padding_length]

def encrypt_file(input_file, output_file, key):
    """
    Encrypt a file using AES in CBC mode.
    """
    cipher = AES.new(key, AES.MODE_CBC)
    with open(input_file, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            f_out.write(cipher.iv)
            while True:
                chunk = f_in.read(16)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk = pad(chunk)
                f_out.write(cipher.encrypt(chunk))

def decrypt_file(input_file, output_file, key):
    """
    Decrypt a file using AES in CBC mode.
    """
    with open(input_file, 'rb') as f_in:
        iv = f_in.read(16)
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
        with open(output_file, 'wb') as f_out:
            decrypted_data = b''
            while True:
                chunk = f_in.read(16)  # Read 16 bytes at a time
                if not chunk:
                    break  # End of file
                
                decrypted_chunk = cipher.decrypt(chunk)
                decrypted_data += decrypted_chunk
            
            # Unpad the decrypted data
            unpadded_data = unpad(decrypted_data)
            
            # Write the decrypted and unpadded data to the output file
            f_out.write(unpadded_data)

# Example usage:
key = get_random_bytes(16)  # Generate a random 128-bit key
input_file = 'input.txt'
encrypted_file = 'encrypted_file.enc'
decrypted_file = 'decrypted_file.txt'

# Encrypt the file
encrypt_file(input_file, encrypted_file, key)

# Decrypt the file
decrypt_file(encrypted_file, decrypted_file, key)