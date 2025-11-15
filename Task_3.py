# assistant_bot.py

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "This contact does not exist."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command"
    return inner


@input_error
def add_contact(args, contacts):
    # очікуємо: args -> [name, phone]
    name, phone = args  # ValueError якщо аргументів не 2
    contacts[name] = phone
    return f"Contact {name} added."


@input_error
def change_contact(args, contacts):
    # очікуємо: args -> [name, phone]
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return f"Phone number for {name} changed."


@input_error
def get_phone(args, contacts):
    # Зайва явна перевірка не потрібна — contacts[name] підкине KeyError
    name = args[0]  # IndexError якщо args пустий
    return f"{name}: {contacts[name]}"


@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def parse_input(user_input: str):
    """Повертає (command, args). Якщо пустий рядок — повертає (None, [])."""
    parts = user_input.strip().split()
    if not parts:
        return None, []
    command = parts[0].lower()
    args = parts[1:]
    return command, args


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    print("Available commands: add, change, phone, all, exit")

    while True:
        raw = input("Enter a command: ")
        command, args = parse_input(raw)

        # якщо користувач просто натиснув Enter
        if command is None:
            print("Please type a command (add, change, phone, all, exit).")
            continue

        # підтримка декількох варіантів виходу
        if command in ("exit", "close", "bye", "goodbye", "good"):
            print("Good bye!")
            break

        # ТУТ — ключова логіка: ми порівнюємо перше слово (command),
        # а аргументи беремо з args. Саме це забезпечує, що рядок
        # "add a 1" сприйматиметься як команда add з аргументами.
        if command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Unknown command. Please try again.")


if __name__ == "__main__":
    main()
