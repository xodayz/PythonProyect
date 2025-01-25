def numberSense():
    num = int(input("Digit a number:"))
    if num < 0:
        print("Negative number dude")
    else:
        print("Possitive number dude")

def digitsByNumber():
    num = int(input("Digit a number: "))
    num = abs(num)

    count = 0
    while num > 0:
        num //= 10
        count += 1
    print(f"El numero tiene {count} digitos.")

def primeNumber():
    x1 = int(input("Digit a numbere:"))
    if x1 <= 1:
        print("Negative numbers is not valid dude")
    elif 2 <= x1 <= 3:
        print("Prime number")
    elif x1 % 2 == 0:
        print("Not prime number")
    else:
        print("Prime number")

def maxNumberInList():
    nums = 0
    storage = []
    while nums < 4:
        nums += 1
        number = int(input("Digit any number pls: "))
        storage.append(number)

    max_num = storage[0]
    for n in storage:
        if n > max_num:
            max_num = n
    print(storage)
    print(f"El numero mayor es: {max_num}")

def listWithoutDuplicates():
    numeros = [1, 1, 2, 3, 3, 2, 5, 6, 2, 7, 8, 4, 3, 1]
    numeros_unicos = set(numeros)
    print(f"Original list: {numeros}")
    print(f"List without duplicates: {sorted(numeros_unicos)}")


def menu():
    while True:
        print("\nMENU")
        print("1. Number Sense")
        print("2. Count Digits in a Number")
        print("3. Check Prime Number")
        print("4. Ass and Find Max in a List")
        print("5. Remove Duplicates from a List")
        print("6. Exit")

        try:
            selector = int(input("Select an option (1-6): "))
            if selector == 1:
                numberSense()
            elif selector == 2:
                digitsByNumber()
            elif selector == 3:
                primeNumber()
            elif selector == 4:
                maxNumberInList()
            elif selector == 5:
                listWithoutDuplicates()
            elif selector == 6:
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

# Start the program
menu()