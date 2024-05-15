import hashlib

class HashPRNG:
    def __init__(self, seed):
        self.seed = seed
    
    def generate_random(self):
        # Преобразуем сид в байтовую строку
        seed_bytes = str(self.seed).encode('utf-8')
        
        # Получаем хеш сида
        hash_value = hashlib.sha256(seed_bytes).hexdigest()
        
        # Обновляем сид с использованием хеша
        self.seed = hash_value
        
        # Возвращаем целочисленное значение хеша
        return int(hash_value, 16)

# Пример использования
prng = HashPRNG(seed=12345)
for _ in range(5):
    print(prng.generate_random())