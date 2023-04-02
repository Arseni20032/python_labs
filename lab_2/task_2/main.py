from Container import *


def main():
    _cont = Container()

    print("Enter your username to make possible to load your last container: ")
    name = input()
    _cont.add_users(name)
    _cont.load()

    choose_menu = "Menu:\n 1. Add element\n 2. Remove\n 3. Find key\n 4. Print list\n 5. Grep\n" \
                  " 6. Save\n 7. Load\n 8. Switch user\n 9. Exit\n"

    while True:
        print(choose_menu)
        decision = input()

        if decision == "1":
            print("Enter the element: ")
            _cont.add(input())
        elif decision == "2":
            print("Enter the element: ")
            _cont.remove(input())
        elif decision == "3":
            print("Enter the element: ")
            _cont.find(input())
        elif decision == "4":
            print("Printing...")
            _cont.print_fun()
        elif decision == "5":
            print("Enter regex to match: ")
            _cont.grep(input())
        elif decision == "6":
            print("Saving...")
            _cont.save()
        elif decision == "7":
            print("Load...")
            _cont.load()
        elif decision == "8":
            print("Enter the name of user to switch: ")
            _cont.change_users(input())
        elif decision == "9":
            break
        else:
            print("Error! Please, try again!\n")
            continue


if __name__ == "__main__":
    main()
