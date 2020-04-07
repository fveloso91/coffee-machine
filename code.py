# Write your code here


def espresso(w, b, c):
    cups_posible = [int(w / 250), int(b / 16)]

    posible_cups = cups_posible[0]
    for cup in cups_posible:
        if cup <= posible_cups:
            posible_cups = cup

    num_cups = c

    if (posible_cups and num_cups) > 0:
        print("I have enough resources, making you a coffee!")
        c -= 1
        w -= 250
        b -= 16

    else:
        if cups_posible[0] == 0:
            print("Sorry, not enough water!")
        elif cups_posible[1] == 0:
            print("Sorry, not enough beans!")
        elif num_cups == 0:
            print("Sorry, not enough cups!")

    return w, b, c


def latte(w, m, b, c):
    cups_posible = [int(w / 350), int(m / 75), int(b / 20)]

    posible_cups = cups_posible[0]
    for cup in cups_posible:
        if cup <= posible_cups:
            posible_cups = cup

    num_cups = cups

    if (posible_cups and num_cups) > 0:
        print("I have enough resources, making you a coffee!")
        c -= 1
        w -= 350
        m -= 75
        b -= 20
    else:
        if cups_posible[0] == 0:
            print("Sorry, not enough water!")
        elif cups_posible[1] == 0:
            print("Sorry, not enough milk!")
        elif cups_posible[2] == 0:
            print("Sorry, not enough beans!")
        elif num_cups == 0:
            print("Sorry, not enough cups!")

    return w, m, b, c


def cappuccino(w, m, b, c):
    cups_posible = [int(w / 200), int(m / 100), int(b / 12)]

    posible_cups = cups_posible[0]
    for cup in cups_posible:
        if cup <= posible_cups:
            posible_cups = cup

    num_cups = c

    if (posible_cups and num_cups) > 0:
        print("I have enough resources, making you a coffee!")
        c -= 1
        w -= 200
        m -= 100
        b -= 12

    else:
        if cups_posible[0] == 0:
            print("Sorry, not enough water!")
        elif cups_posible[1] == 0:
            print("Sorry, not enough milk!")
        elif cups_posible[2] == 0:
            print("Sorry, not enough beans!")
        elif num_cups == 0:
            print("Sorry, not enough cups!")

    return w, m, b, c


def message(w, m, b, c, mo):
    print("The coffee machine has:")
    print(w, " of water")
    print(m, " of milk")
    print(b, " of coffee beans")
    print(c, " of disposable cups")
    print("$" + str(mo) + " of money")


def action(a, w, m, b, c, mo):
    if a == "buy":
        user_input = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        if user_input == "1":
            w, b, c = espresso(w, b, c)
            mo += 4
        elif user_input == "2":
            w, m, b, c = latte(w, m, b, c)
            mo += 7
        elif user_input == "3":
            w, m, b, c = cappuccino(w, m, b, c)
            mo += 6
        elif user_input == "back":
            return w, m, b, c, mo

    elif a == "fill":
        print("merda")
        w += int(input("Write how many ml of water do you want to add: "))
        m += int(input("Write how many ml of milk do you want to add: "))
        b += int(input("Write how many grams of coffee beans do you want to add: "))
        c += int(input("Write how many disposable cups of coffee do you want to add: "))

    elif a == "take":
        print("I gave you $", mo)
        mo = 0

    else:
        print("Try again, wrong input")

    return w, m, b, c, mo


print("Starting to make a coffee")
print("Grinding coffee beans")
print("Boiling water")
print("Mixing boiled water with crushed coffee beans")
print("Pouring coffee into the cup")
print("Pouring some milk into the cup")
print("Coffee is ready!")

money = 550
water = 400
milk = 540
beans = 120
cups = 9

while True:
    intro = str(input("Write action (buy, fill, take, remaining, exit): "))
    if intro == "remaining":
        message(water, milk, beans, cups, money)
        continue
    elif intro == "buy" or intro == "fill" or intro == "take":
        water, milk, beans, cups, money = action(intro, water, milk, beans, cups, money)
        continue
    elif intro == "exit":
        break
