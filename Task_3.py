
# Декоратор для обробки помилок користувацького вводу
def input_error(func):

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "This contact does not exist."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
    return inner


# Команди бота
@input_error
def add_contact(args, contacts):
    #  Додає новий контакт у словник 
    name, phone = args  # може викликати ValueError, якщо немає двох аргументів
    contacts[name] = phone
    return f"Contact {name} added."


@input_error
def change_contact(args, contacts):
    # Змінює номер телефону для існуючого контакту 
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return f"Phone number for {name} changed."


@input_error
def get_phone(args, contacts):
    # Повертає номер телефону для заданого контакту
    name = args[0]
    if name not in contacts:
        raise KeyError
    return f"{name}: {contacts[name]}"


@input_error
def show_all(contacts):
    # Виводить усі збережені контакти 
    if not contacts:
        return "No contacts found."
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)



def main():
    # Основна функція для запуску консольного бота 
    contacts = {}

    print("Welcome to the assistant bot!")
    print("Available commands: add, change, phone, all, exit")

    while True:
        command = input("Enter a command: ").strip().lower()

        if command in ["exit", "close", "good bye"]:
            print("Good bye!")
            break

        elif command == "add":
            args = input("Enter name and phone: ").strip().split()
            print(add_contact(args, contacts))

        elif command == "change":
            args = input("Enter name and new phone: ").strip().split()
            print(change_contact(args, contacts))

        elif command == "phone":
            args = input("Enter name: ").strip().split()
            print(get_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Unknown command. Please try again.")


# Точка входу
if __name__ == "__main__":
    main()
