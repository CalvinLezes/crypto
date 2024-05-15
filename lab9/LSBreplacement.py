from PIL import Image

# Embeds text message into an image using LSB replacement
def embed_message(image_path, message):
    img = Image.open(image_path)
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    if len(binary_message) > img.width * img.height * 3:
        raise ValueError("Message is too long to be embedded in the image")
    
    data_index = 0
    for y in range(img.height):
        for x in range(img.width):
            pixel = list(img.getpixel((x, y)))
            for i in range(3):
                if data_index < len(binary_message):
                    pixel[i] = pixel[i] & 0xFE | int(binary_message[data_index])
                    data_index += 1
            img.putpixel((x, y), tuple(pixel))
    img.save("stego_image.bmp")

# Extracts text message from an image using LSB replacement
def extract_message(image_path):
    img = Image.open(image_path)
    binary_message = ""
    for y in range(img.height):
        for x in range(img.width):
            pixel = img.getpixel((x, y))
            for i in range(3):
                binary_message += str(pixel[i] & 1)
    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        message += chr(int(byte, 2))
        if message.endswith('\0'):  # End of message character
            break
    return message.rstrip('\0')


embed_message("original.bmp", "This is a secret message89347892476659843266594326975643272655472365423790\0")

# Extracting message from stego image
extracted_message = extract_message("stego_image.bmp")
print("Extracted message:", extracted_message)