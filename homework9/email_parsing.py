import re

def split_email(email):
    pattern = r'([a-zA-Z][\w\.-]*)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'
    match = re.match(pattern, email)

    if match:
        username = match.group(1)
        domain = match.group(2)
        return username, domain
    else:
        return None, None

def main():
    email = input("Введите email: ")
    username, domain = split_email(email)

    if username and domain:
        print(f"Username: {username}")
        print(f"Domain: {domain}")
    else:
        print("Неккоректный email.")

if __name__ == "__main__":
    main()