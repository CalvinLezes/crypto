import sympy
import secrets
import itertools

def to_binary(number):
    binary_representation = []

    # Обрабатываем случай нуля отдельно
    if number == 0:
        return [0]

    while number > 0:
        remainder = number % 2
        binary_representation.insert(0, remainder)  # Вставляем остаток в начало списка
        number //= 2

    binary_representation.reverse()
    return binary_representation

# Быстрое возведение в степень
def mod_exp(base, exponent, modulus):

    # Инициализируем счетчик умножений
    global multiplication_counter
    multiplication_counter = 0
    
    def mod_mul(x, y, mod):
        # Вспомогательная функция для умножения с модулем
        global multiplication_counter
        multiplication_counter += 1
        res = (x * y) % mod
        return res

    s = base
    y = 1
    exponent_binary = to_binary(exponent)
    for x in exponent_binary:
        if x == 1:
            y = mod_mul(y, s, modulus)
        s = mod_mul(s, s, modulus)
    return y

# Генерация случайного секретного ключа
def generate_secret_key(bits):
    return secrets.randbelow(2**bits - 1) + 1  # Генерация числа от 1 до 2^k - 1

# Выбор параметров p, g и генерация секретных ключей
def setup_system(N, k):
    # Шаг 1: Генерация простого числа q
    q = sympy.prime(secrets.randbelow(100))  # Генерация случайного простого числа q (для упрощения)
    p = 2 * q + 1  # Вычисление p = 2q + 1

    # Шаг 2: Выбор генератора g
    g = find_g(q)

    # Шаг 3: Генерация секретных ключей для каждого абонента
    secret_keys = [generate_secret_key(k) for _ in range(N)]

    # Шаг 4: Вычисление открытых ключей
    public_keys = [mod_exp(g, secret_key, p) for secret_key in secret_keys]

    return p, g, secret_keys, public_keys

# Реализация поиска генератора g
def find_g(q):
    p = 2 * q + 1
    for g in range(2, p):
        if mod_exp(g, q, p) > 1:
            return g
    return None

# Основная функция для вычисления общего секрета
def compute_shared_secrets(N, p, public_keys, secret_keys):
    shared_secrets = {}
    for i, j in itertools.combinations(range(N), 2):
        # Абонент i вычисляет Z_ij
        Z_ij = mod_exp(public_keys[j], secret_keys[i], p)
        # Абонент j вычисляет Z_ji
        Z_ji = mod_exp(public_keys[i], secret_keys[j], p)
        shared_secrets[(i, j)] = (Z_ij, Z_ji)

    return shared_secrets

# Ввод от пользователя
N = int(input("Введите количество абонентов: "))
k = int(input("Введите длину секретных ключей в битах: "))

# Настройка системы
p, g, secret_keys, public_keys = setup_system(N, k)

# Выводим параметры системы
print(f"\np = {p}, g = {g}\n")
print("Таблица с ключами абонентов:")
print(f"{'Абонент':<10}{'Секретный ключ':<20}{'Открытый ключ'}")
for i in range(N):
    print(f"{i:<10}{secret_keys[i]:<20}{public_keys[i]}")

# Вычисляем общие секреты
shared_secrets = compute_shared_secrets(N, p, public_keys, secret_keys)

# Выводим общие секреты
print("\nОбщие секретные ключи:")
for (i, j), (Z_ij, Z_ji) in shared_secrets.items():
    print(f"Для абонентов {i} и {j}: Z_ij = {Z_ij}, Z_ji = {Z_ji}")
