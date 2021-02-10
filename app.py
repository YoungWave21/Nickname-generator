import random

nicknames = ["Doobie", "Matey", "Hammer", "Lion", "Boo", "PB&J", "Chicken Wing", "Twinkly", "Donuts", "Bunny Rabbit",
             "Snickers", "Dearey"]


class Name:
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last
        self.nickname = nicknames[random.randint(0, len(nicknames) - 1)]

    def print_name(self):
        print(f'Hi {self.first_name} "{self.nickname}" {self.last_name}')

    def change_name(self):
        self.first_name = input("Please enter your first name: ").capitalize()
        self.last_name = input("Please enter your last name: ").capitalize()
        self.print_name()

    def display_all(self):
        print(f'Here are a list of all possible nicknames')
        for i in range(len(nicknames)):
            print(f'"{nicknames[i].capitalize()}"')

    def display_random(self):
        print(f'Here is a random nickname: {nicknames[random.randint(0, len(nicknames) - 1)].capitalize()}')

    def add(self):
        name = input("The nickname you would like to add is: ")
        if not name.isnumeric():
            nicknames.append(name)

    def remove(self):
        name = input("The nickname you would like to remove is: ")
        found = False
        for i in range(len(nicknames) - 1):
            if name.lower() == nicknames[i].lower():
                nicknames.pop(i)
                found = True
                print("Nickname removed!")
        if not found:
            print("Nickname not found :(")
            self.remove()


def main():
    first_name = input("Please enter your first name: ").capitalize()
    last_name = input("Please enter your last name: ").capitalize()
    person = Name(first_name, last_name)
    person.print_name()
    while True:
        print("______________________________")
        print("1. Change Name")
        print("2. Display a Random Nickname")
        print("3. Display All Nicknames")
        print("4. Add a Nickname")
        print("5. Remove a Nickname")
        print("6. Exit")
        print("______________________________")
        choice = int(input("Your choice: "))
        if 0 < choice < 7:
            options = {
                1: person.change_name,
                2: person.display_random,
                3: person.display_all,
                4: person.add,
                5: person.remove,
                6: exit,
            }
            options[choice]()
        else:
            print("The option you have selected does not exist!")


main()
