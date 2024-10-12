import math

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: Введите корректное число!")

def get_squares_between(a, b):
    start = math.ceil(min(a, b))
    end = math.floor(max(a, b))

    if a == start:
        start += 1
    if b == end:
        end -= 1

    return [i**2 for i in range(start, end + 1)]

while True:
    print("\nВведите два числа (a и b) для рассчета квадратов целых чисел между ними.")

    a = get_float_input("Введите число a: ")
    b = get_float_input("Введите число b: ")

    squares = get_squares_between(a, b)

    if squares:
        print(f"Квадраты целых чисел между {a} и {b}: {squares}")
    else:
        print(f"Нет целых чисел между {a} и {b}")

    continue_input = input("\nХотите ввести другие числа? (да/нет): ").strip().lower()
    if continue_input != "да":
        print("Программа завершена.")
        break