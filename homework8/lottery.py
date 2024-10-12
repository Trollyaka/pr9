import random

ticket = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]

def get_user_numbers():
    user_numbers = []
    for i, row in enumerate(ticket):
        while True:
            try:
                number = int(input(f"Выберите число из строки {i + 1} {row}: "))
                if number in row:
                    user_numbers.append(number)
                    break
                else:
                    print("Число не найдено в строке. Пожалуйста, попробуйте снова.")
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите число.")
    return user_numbers

def draw_computer_numbers():
    computer_numbers = []
    for row in ticket:
        number = random.choice(row)
        computer_numbers.append(number)
    return computer_numbers

def calculate_statistics(user_numbers, computer_numbers):
    matches = set(user_numbers) & set(computer_numbers)
    return len(matches), matches

def get_match_word(count):
    if count == 1:
        return "число"
    elif 2 <= count <= 4:
        return "числа"
    else:
        return "чисел"

def main():
    print("Добро пожаловать в лотерею!")

    user_numbers = get_user_numbers()
    drawn_numbers = draw_computer_numbers()

    print(f"\nВы выбрали числа: {user_numbers}")
    print(f"Случайно выбранные числа: {drawn_numbers}")

    match_count, matches = calculate_statistics(user_numbers, drawn_numbers)

    match_word = get_match_word(match_count)

    if match_count == 0:
        print(f"\nК сожалению, вы не угадали ни одного числа.")
    else:
        print(f"\nВы угадали {match_count} {match_word}: {matches}")

if __name__ == "__main__":
    main()