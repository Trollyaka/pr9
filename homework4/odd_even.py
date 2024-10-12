numbers = []
while True:
    user_input = input("Введите число (или 'end' для завершения): ")
    if user_input.lower() == "end":
        break
    try:
        number = int(user_input)
        numbers.append(number)
    except ValueError:
        print("Некорректное значение. Попробуйте ещё раз.")

even_count = sum(1 for num in numbers if num % 2 == 0)
odd_count = len(numbers) - even_count

print(f"Количество четных чисел: {even_count}")
print(f"Количество нечетных чисел: {odd_count}")