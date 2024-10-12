numbers = []

while True:
    user_input = input("Введите число (или 'end' для завершения): ")

    if user_input.lower() == 'end':
        break

    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Некорректное значение. Попробуйте ещё раз.")

odd_numbers = [int(num) for num in numbers if num.is_integer() and int(num) % 2 != 0]
print("Нечётные числа:", odd_numbers)