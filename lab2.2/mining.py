import hashlib
import time

# Функция для вычисления хеша
def hash_function(value_nonce):
    return hashlib.sha256(value_nonce.encode('utf-8')).hexdigest()

# Функция для нахождения нужного k
def find_k(target_time, value):
    print("Calculating optimal k")
    # Начальная сложность (к примеру, k = 1)
    k = 1
    # Сложность с максимальной маской (полностью 256 единичных бит)
    max_k = 256
    optimal_k = k

    while k <= max_k:
        mask = (2**k - 1) << (256 - k)  # Генерация маски для k битов
        total_time = 0
        trials = 3  # Количество испытаний для более точного времени
        
        # Пробуем несколько раз найти блок с данным значением k
        for _ in range(trials):
            nonce = 0
            start_time = time.time()
            while True:
                nonce += 1
                value_nonce = f"{value}|{nonce}"
                hash_result = hash_function(value_nonce)

                # Преобразуем хеш в битовую строку
                hash_bits = bin(int(hash_result, 16))[2:].zfill(256)

                # Применяем маску для проверки
                if int(hash_bits, 2) & mask == 0:
                    end_time = time.time()
                    total_time += (end_time - start_time)
                    break
        

        # Проверяем, близко ли среднее время к целевому
        avg_time = total_time / trials
        #print(avg_time)
        if avg_time >= target_time:
            optimal_k = k
            break
        else:
            k += 1  # Увеличиваем сложность (количество нулевых бит)

    return optimal_k

# Функция майнинга
def mine_block(k, value):
    
    mask = (2**k - 1) << (256 - k)  # Генерация маски, где k - количество единичных битов

    # Начинаем майнинг с найденным значением k
    print(f"Starting mining with k={k}...")
    nonce = 0
    start_time = time.time()

    while True:
        nonce += 1
        value_nonce = f"{value}|{nonce}"
        hash_result = hash_function(value_nonce)

        # Преобразуем хеш в битовую строку
        hash_bits = bin(int(hash_result, 16))[2:].zfill(256)

        # Применяем маску для проверки
        if int(hash_bits, 2) & mask == 0:
            end_time = time.time()
            mining_time = end_time - start_time
            print(f"Block mined with NONCE: {nonce}. Time taken: {mining_time:.4f} seconds")
            return nonce

# Основная часть программы
if __name__ == "__main__":
    target_time = float(input("Enter target time to mine one block (in seconds): "))
    value = "0203"  # Время или данные для блока
    k = find_k(target_time, value)  # Находим подходящее значение k
    while True:
        print(f"Starting mining for block with target time {target_time} seconds...")
        nonce = mine_block(k, value)
        #print(f"Block mined with NONCE: {nonce}\n")
