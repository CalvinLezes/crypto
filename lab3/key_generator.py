import random
import string

def generate_random_char():
    return random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)

with open('random_key.txt', 'w') as f:
    random_chars = ''.join(generate_random_char() for _ in range(2000))
    f.write(random_chars)