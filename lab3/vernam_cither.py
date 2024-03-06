def xor_files(file1_path, file2_path, output_path):
    with open(file1_path, 'rb') as file1, open(file2_path, 'rb') as file2, open(output_path, 'wb') as output_file:
        while True:
            byte1 = file1.read(1)
            byte2 = file2.read(1)

            if not byte1 or not byte2:
                break

            xor_result = bytes([byte1[0] ^ byte2[0]])
            output_file.write(xor_result)

key_path = 'D:/crypto/random_key.txt'
file_path = 'D:/crypto/open_text.txt'
cither_path = 'lab3/xor_result.txt'
decither_path = 'lab3/decither_result.txt'
xor_files(file_path, key_path, cither_path)
xor_files(cither_path, key_path, decither_path)