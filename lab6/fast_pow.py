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

def mod_exp(base, exponent, modulus):

    # Инициализируем счетчик умножений
    global multiplication_counter
    multiplication_counter = 0
    
    def mod_mul(x, y, mod):
        # Вспомогательная функция для умножения с модулем
        global multiplication_counter
        multiplication_counter += 1
        res = (x * y) % mod
        #print(f"{x}^{y} mod {mod} = {res}")
        return res

    s = base
    y = 1
    exponent_binary = to_binary(exponent)
    print(exponent_binary)
    for x in exponent_binary:
        print('x ', x)
        if x == 1:
            y = mod_mul(y, s, modulus)
            print('y ', y)
        print('s ', s)
        s = mod_mul(s, s, modulus)
    return y

# Пример использования
#base = 5
#exponent = 701
#modulus = 11

base = int(input("Введите число: ").strip())
exponent = int(input("Введите степень: ").strip())
modulus = int(input("Введите модуль: ").strip())

result = mod_exp(base, exponent, modulus)

print(f"{base}^{exponent} mod {modulus} = {result}")
print(f"Количество умножений: {multiplication_counter}")