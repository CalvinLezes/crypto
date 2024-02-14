def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Определение сдвига для символа
            shifted = ord(char) + shift
            # Обработка границ алфавита
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            # Добавление зашифрованного символа в строку
            encrypted_text += chr(shifted)
        else:
            # Оставляем символы, которые не являются буквами без изменений
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def caesar_attack(plaintext, ciphertext):
    # Предполагаем, что оба текста имеют одинаковую длину
    shift = ord(ciphertext[0]) - ord(plaintext[0])
    # Проверяем, если сдвиг выходит за границы алфавита
    if shift < 0:
        shift += 26
    return shift

def caesar_brute_force(ciphertext):
    decrypted_texts = []
    for shift in range(26):
        decrypted_text = ""
        decrypted_text = caesar_cipher_decrypt(ciphertext, shift)
        decrypted_texts.append(decrypted_text)
    return decrypted_texts

# Список известных слов или фраз
KNOWN_WORDS = {"the", "and", "of", "to", "in", "that", "it", "is", "was", "for", "hello"}

def caesar_brute_force_with_dictionary(ciphertext):
    max_matches = 0
    best_key = 0
    best_decrypted_text = ""

    for shift in range(26):
        decrypted_text = ""
        matches = 0
        
        decrypted_text = caesar_cipher_decrypt(ciphertext, shift)

        # Подсчет совпадений с известными словами
        for word in KNOWN_WORDS:
            if word in decrypted_text.lower():
                matches += 1

        # Обновление лучшего ключа
        if matches > max_matches:
            max_matches = matches
            best_key = shift
            best_decrypted_text = decrypted_text

    return best_key, best_decrypted_text

mode = input("Если хотите зашифровать текст, нажмите 0;\nЕсли хотите совершить атаку по открытому тексту, нажмите 1\nЕсли хотите совершить атаку по шифрованному тексту, нажмите 2\n").strip()
if(mode == "0"):
    text = input("Введите текст, который хотите зашифровать: ").strip()
    shift = int(input("Введите ключ шифрования: ").strip())
    ciphertext = caesar_cipher_encrypt(text, shift)
    print("Зашифрованный текст: ", ciphertext)
if(mode == "1"):
    plaintext = input("Введите открытый текст: ").strip()
    ciphertext = input("Введите зашифрованный текст: ").strip()

    key = caesar_attack(plaintext, ciphertext)
    print("Ключ шифрования:", key)
if(mode == "2"):
    ciphertext = input("Введите зашифрованный текст: ").strip()

    best_key, best_decrypted_text = caesar_brute_force_with_dictionary(ciphertext)

    print("Лучший ключ шифрования:", best_key)
    print("Расшифрованный текст:", best_decrypted_text)