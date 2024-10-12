import random

def generate_random_list(size, lower_bound, upper_bound):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]

def input_size(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Значение должно быть положительным.")
        except ValueError:
            print("Неккоректный ввод. Введите целое положительное число.")

def input_bounds():
    while True:
        try:
            lower_bound = int(input("Введите нижнюю границу для случайных чисел: "))
            upper_bound = int(input("Введите верхнюю границу для случайных чисел: "))
            if lower_bound < upper_bound:
                return lower_bound, upper_bound
            else:
                print("Нижняя граница должна быть меньше верхней.")
        except ValueError:
            print("Неккоректный ввод. Введите целые положительные числа.")

def swap_min_max(lst):
    if not lst:
        return lst
    
    min_value = min(lst)
    max_value = max(lst)

    for i in range(len(lst)):
        if lst[i] == min_value:
            lst[i] = max_value
        elif lst[i] == max_value:
            lst[i] = min_value

    return lst

size = input_size("Введите размер списка: ")

lower_bound, upper_bound = input_bounds()

numbers = generate_random_list(size, lower_bound, upper_bound)
print("Сгенерирванный список: ", numbers)

swapped_list = swap_min_max(numbers)
print("Список после замены местами всех минимальных и максимальных:", swapped_list)