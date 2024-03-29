import heapq

class Monday():
    def __init__(self, description, price, calories, allergies, vegan):
        self.description = description
        self.price = price
        self.calories = calories
        self.allergies = allergies
        self.vegan = vegan


mb1 = Monday("Scrambled Eggs with bacon", 1.50, 250, "eggs", "no")
mb2 = Monday("Toast with butter and strawberry jam", 2, 250, "none", "yes")
# Lunch
ml1 = Monday("Beef with Broccoli and rice", 5, 450, "none", "no")
ml2 = Monday("Ravioli filled with spinach and roasted tomato sauce ", 6, 350, "none", "yes")
# Dinner
md1 = Monday("Risotto with bacon and parmesan cheese ", 5, 250, "none", "no")
md2 = Monday("Salmon with boiled potatoes", 6, 350, "none", "yes")


class Tuesday():
    def __init__(self, description, price, calories, allergies, vegan):
        self.description = description
        self.price = price
        self.calories = calories
        self.allergies = allergies
        self.vegan = vegan


tb1 = Tuesday("Boiled Eggs with sausages", 1.50, 250, "eggs", "no")
tb2 = Tuesday("Toast with olive oil and tomato", 2, 250, "none", "yes")
# Lunch
tl1 = Tuesday("Chicken with Asparagus", 5, 450, "none", "no")
tl2 = Tuesday("Spaghetti with pesto", 6, 350, "none", "yes")
# Dinner
td1 = Tuesday("Lamb with bacon and parmesan cheese ", 5, 250, "none", "no")
td2 = Tuesday("Caesar Salad", 6, 350, "nuts", "yes")


class Wednesday():
    def __init__(self, description, price, calories, allergies, vegan):
        self.description = description
        self.price = price
        self.calories = calories
        self.allergies = allergies
        self.vegan = vegan


# Breakfast
wb1 = Wednesday("Croissant with some hot chocolate", 1.50, 250, "none", "no")
wb2 = Wednesday("Oatmeal with oat milk", 2, 250, "none", "yes")
# Lunch
wl1 = Wednesday("Burger with fries", 5, 450, "none", "no")
wl2 = Wednesday("Vegan Burger with sweet potato fries", 6, 350, "none", "yes")
# Dinner
wd1 = Wednesday("Pheasant with mashed potato", 5, 250, "none", "no")
wd2 = Wednesday("Green Salad", 6, 350, "nuts", "yes")


class Thursday():
    def __init__(self, description, price, calories, allergies, vegan):
        self.description = description
        self.price = price
        self.calories = calories
        self.allergies = allergies
        self.vegan = vegan


# Breakfast
thb1 = Thursday("Pain-au-chocolat with some hot chocolate", 1.50, 250, "none", "no")
thb2 = Thursday("Acaí bowl", 2, 250, "nuts", "yes")
# Lunch
thl1 = Thursday("Curry with beans", 5, 450, "none", "no")
thl2 = Thursday("Mix of roasted vegetables ", 6, 350, "none", "yes")
# Dinner
thd1 = Thursday("Duck with roasted broccoli", 5, 250, "none", "no")
thd2 = Thursday("Vegetable Soup", 6, 350, "nuts", "yes")


class Friday():
    def __init__(self, description, price, calories, allergies, vegan):
        self.description = description
        self.price = price
        self.calories = calories
        self.allergies = allergies
        self.vegan = vegan


# Breakfast
fb1 = Friday("Porridge with honey", 1.50, 250, "none", "no")
fb2 = Friday("Fruit Salad", 2, 250, "none", "yes")
# Lunch
fl1 = Friday("Salad with tomato and mozarella", 5, 450, "none", "no")
fl2 = Friday("Lentel Bolognese", 6, 350, "none", "yes")
# Dinner
fd1 = Friday("Fresh Margherita Pizza", 5, 250, "none", "no")
fd2 = Friday("Spaghetti and vegan meat balls", 6, 350, "none", "yes")


class Saturday():
    def __init__(self, description, price, calories, allergies, vegan):
        self.description = description
        self.price = price
        self.calories = calories
        self.allergies = allergies
        self.vegan = vegan


# Breakfast
sb1 = Saturday("Bacon Omelette", 1.50, 250, "none", "no")
sb2 = Saturday("Vegan Pancakes with fruits", 2, 250, "none", "yes")
# Lunch
sl1 = Saturday("Beef Stroganoff", 5, 450, "none", "no")
sl2 = Saturday("Vegan Tikka Masala", 6, 350, "none", "yes")
# Dinner
sd1 = Saturday("Shrimp with Rice", 5, 250, "none", "no")
sd2 = Saturday("Butternut Squash Risotto with spinach", 6, 350, "none", "yes")


class Sunday():
    def __init__(self, description, price, calories, allergies, vegan):
        self.description = description
        self.price = price
        self.calories = calories
        self.allergies = allergies
        self.vegan = vegan


# Breakfast
xb1 = Sunday("Cinamon Rolls", 1.50, 250, "none", "no")
xb2 = Sunday("Homemade Granola", 2, 250, "none", "yes")
# Lunch
xl1 = Sunday("Taco Wraps", 5, 450, "none", "no")
xl2 = Sunday("Vegan Ratatouille", 6, 350, "none", "yes")
# Dinner
xd1 = Sunday("Turkey Salad with Pear Dressing", 5, 250, "none", "no")
xd2 = Sunday("Carrot Miso Pasta", 6, 350, "none", "yes")


def daily():
    while True:
        day_of_week = input("\nPlease enter what weekday would you like to receive your menu: ")
        if day_of_week == "monday":
            print("\nFor breakfast:")
            print("1.", mb1.description)
            print("2.", mb2.description)
            print("\nFor lunch:")
            print("1.", ml1.description)
            print("2.", ml2.description)
            print("\nFor dinner:")
            print("1.", md1.description)
            print("2.", md2.description)
            break
        elif day_of_week == "tuesday":
            print("\nFor breakfast:")
            print("1.", tb1.description)
            print("2.", tb2.description)
            print("\nFor lunch:")
            print("1.", tl1.description)
            print("2.", tl2.description)
            print("\nFor dinner:")
            print("1.", td1.description)
            print("2.", td2.description)
            break
        elif day_of_week == "wednesday":
            print("\nFor breakfast:")
            print("1.", wb1.description)
            print("2.", wb2.description)
            print("\nFor lunch:")
            print("1.", wl1.description)
            print("2.", wl2.description)
            print("\nFor dinner:")
            print("1.", wd1.description)
            print("2.", wd2.description)
            break
        elif day_of_week == "thursday":
            print("\nFor breakfast:")
            print("1.", thb1.description)
            print("2.", thb2.description)
            print("\nFor lunch:")
            print("1.", thl1.description)
            print("2.", thl2.description)
            print("\nFor dinner:")
            print("1.", thd1.description)
            print("2.", thd2.description)
            break
        elif day_of_week == "friday":
            print("\nFor breakfast:")
            print("1.", fb1.description)
            print("2.", fb2.description)
            print("\nFor lunch:")
            print("1.", fl1.description)
            print("2.", fl2.description)
            print("\nFor dinner:")
            print("1.", fd1.description)
            print("2.", fd2.description)
            break
        elif day_of_week == "saturday":
            print("\nFor breakfast:")
            print("1.", sb1.description)
            print("2.", sb2.description)
            print("\nFor lunch:")
            print("1.", sl1.description)
            print("2.", sl2.description)
            print("\nFor dinner:")
            print("1.", sd1.description)
            print("2.", sd2.description)
            break
        elif day_of_week == "sunday":
            print("\nFor breakfast:")
            print("1.", xb1.description)
            print("2.", xb2.description)
            print("\nFor lunch:")
            print("1.", xl1.description)
            print("2.", xl2.description)
            print("\nFor dinner:")
            print("1.", xd1.description)
            print("2.", xd2.description)
            break
        else:
            print("Invalid input! Please try again.")

    while True:
        selectionlist = ['1 1 1', '1 1 2', '1 2 1', '1 2 2', '2 1 1', '2 1 2', '2 2 1', '2 2 2']
        selection = input("\nChoose one option from each meal (breakfast, lunch, dinner)"
                          "\nand enter each number with a space(ex:1 2 1): ")
        if selection in selectionlist:
            break
        else:
            print("\nInvalid input! Please try again")
    else:
        print("Invalid input! Please try again")

    while True:
        try:
            b, l, d = selection.split()
            if day_of_week == "monday":
                print("\nYou have chosen the following options:")
                if b == "1":
                    print(mb1.description)
                elif b == "2":
                    print(mb2.description)
                if l == "1":
                    print(ml1.description)
                elif l == "2":
                    print(ml2.description)
                if d == "1":
                    print(md1.description)
                elif d == "2":
                    print(md2.description)
            if day_of_week == "tuesday":
                print("\nYou have chosen the following options:")
                if b == "1":
                    print(tb1.description)
                elif b == "2":
                    print(tb2.description)
                if l == "1":
                    print(tl1.description)
                elif l == "2":
                    print(tl2.description)
                if d == "1":
                    print(td1.description)
                elif d == "2":
                    print(td2.description)
            if day_of_week == "wednesday":
                print("\nYou have chosen the following options:")
                if b == "1":
                    print(wb1.description)
                elif b == "2":
                    print(wb2.description)
                if l == "1":
                    print(wl1.description)
                elif l == "2":
                    print(wl2.description)
                if d == "1":
                    print(wd1.description)
                elif d == "2":
                    print(wd2.description)
            if day_of_week == "thursday":
                print("\nYou have chosen the following options:")
                if b == "1":
                    print(thb1.description)
                elif b == "2":
                    print(thb2.description)
                if l == "1":
                    print(thl1.description)
                elif l == "2":
                    print(thl2.description)
                if d == "1":
                    print(thd1.description)
                elif d == "2":
                    print(thd2.description)
            if day_of_week == "friday":
                print("\nYou have chosen the following options:")
                if b == "1":
                    print(fb1.description)
                elif b == "2":
                    print(fb2.description)
                if l == "1":
                    print(fl1.description)
                elif l == "2":
                    print(fl2.description)
                if d == "1":
                    print(fd1.description)
                elif d == "2":
                    print(fd2.description)
            if day_of_week == "saturday":
                print("\nYou have chosen the following options:")
                if b == "1":
                    print(sb1.description)
                elif b == "2":
                    print(sb2.description)
                if l == "1":
                    print(sl1.description)
                elif l == "2":
                    print(sl2.description)
                if d == "1":
                    print(sd1.description)
                elif d == "2":
                    print(sd2.description)
            if day_of_week == "sunday":
                print("\nYou have chosen the following options:")
                if b == "1":
                    print(xb1.description)
                elif b == "2":
                    print(xb2.description)
                if l == "1":
                    print(xl1.description)
                elif l == "2":
                    print(xl2.description)
                if d == "1":
                    print(xd1.description)
                elif d == "2":
                    print(xd2.description)
            print("\nYour order is ready to be shipped to your closest food locker!")
            break
        except ValueError:
            print("Input error! Please try again.")
    else:
        print("Invalid menu choice! Try again.")


def weekly():
    print("\nChoose a menu for Monday")
    print("\nFor breakfast:")
    print("1.", mb1.description)
    print("2.", mb2.description)
    print("\nFor lunch:")
    print("1.", ml1.description)
    print("2.", ml2.description)
    print("\nFor dinner:")
    print("1.", md1.description)
    print("2.", md2.description)
    while True:
        selectionlist = ['1 1 1', '1 1 2', '1 2 1', '1 2 2', '2 1 1', '2 1 2', '2 2 1', '2 2 2']
        selection_monday = input("\nChoose one option from each meal (breakfast, lunch, dinner)"
                                 "\nand enter each number with a space(ex:1 2 1): ")
        if selection_monday in selectionlist:
            break
        else:
            print("\nInvalid input! Please try again")
    else:
        print("Invalid input! Please try again")
    print("\nChoose a menu for Tuesday")
    print("\nFor breakfast:")
    print("1.", tb1.description)
    print("2.", tb2.description)
    print("\nFor lunch:")
    print("1.", tl1.description)
    print("2.", tl2.description)
    print("\nFor dinner:")
    print("1.", td1.description)
    print("2.", td2.description)
    while True:
        selectionlist = ['1 1 1', '1 1 2', '1 2 1', '1 2 2', '2 1 1', '2 1 2', '2 2 1', '2 2 2']
        selection_tuesday = input("\nChoose one option from each meal (breakfast, lunch, dinner)"
                                 "\nand enter each number with a space(ex:1 2 1): ")
        if selection_tuesday in selectionlist:
            break
        else:
            print("\nInvalid input! Please try again")
    else:
        print("Invalid input! Please try again")
    print("\nChoose a menu for Wednesday")
    print("\nFor breakfast:")
    print("1.", wb1.description)
    print("2.", wb2.description)
    print("\nFor lunch:")
    print("1.", wl1.description)
    print("2.", wl2.description)
    print("\nFor dinner:")
    print("1.", wd1.description)
    print("2.", wd2.description)
    while True:
        selectionlist = ['1 1 1', '1 1 2', '1 2 1', '1 2 2', '2 1 1', '2 1 2', '2 2 1', '2 2 2']
        selection_wednesday = input("\nChoose one option from each meal (breakfast, lunch, dinner)"
                                 "\nand enter each number with a space(ex:1 2 1): ")
        if selection_wednesday in selectionlist:
            break
        else:
            print("\nInvalid input! Please try again")
    else:
        print("Invalid input! Please try again")
    print("\nChoose a menu for Thursday")
    print("\nFor breakfast:")
    print("1.", thb1.description)
    print("2.", thb2.description)
    print("\nFor lunch:")
    print("1.", thl1.description)
    print("2.", thl2.description)
    print("\nFor dinner:")
    print("1.", thd1.description)
    print("2.", thd2.description)
    while True:
        selectionlist = ['1 1 1', '1 1 2', '1 2 1', '1 2 2', '2 1 1', '2 1 2', '2 2 1', '2 2 2']
        selection_thursday = input("\nChoose one option from each meal (breakfast, lunch, dinner)"
                                 "\nand enter each number with a space(ex:1 2 1): ")
        if selection_thursday in selectionlist:
            break
        else:
            print("\nInvalid input! Please try again")
    else:
        print("Invalid input! Please try again")
    print("\nChoose a menu for Friday")
    print("\nFor breakfast:")
    print("1.", fb1.description)
    print("2.", fb2.description)
    print("\nFor lunch:")
    print("1.", fl1.description)
    print("2.", fl2.description)
    print("\nFor dinner:")
    print("1.", fd1.description)
    print("2.", fd2.description)
    while True:
        selectionlist = ['1 1 1', '1 1 2', '1 2 1', '1 2 2', '2 1 1', '2 1 2', '2 2 1', '2 2 2']
        selection_friday = input("\nChoose one option from each meal (breakfast, lunch, dinner)"
                                 "\nand enter each number with a space(ex:1 2 1): ")
        if selection_friday in selectionlist:
            break
        else:
            print("\nInvalid input! Please try again")
    else:
        print("Invalid input! Please try again")

    print("\nChoose a menu for Saturday")
    print("\nFor breakfast:")
    print("1.", sb1.description)
    print("2.", sb2.description)
    print("\nFor lunch:")
    print("1.", sl1.description)
    print("2.", sl2.description)
    print("\nFor dinner:")
    print("1.", sd1.description)
    print("2.", sd2.description)
    while True:
        selectionlist = ['1 1 1', '1 1 2', '1 2 1', '1 2 2', '2 1 1', '2 1 2', '2 2 1', '2 2 2']
        selection_saturday = input("\nChoose one option from each meal (breakfast, lunch, dinner)"
                                 "\nand enter each number with a space(ex:1 2 1): ")
        if selection_saturday in selectionlist:
            break
        else:
            print("\nInvalid input! Please try again")
    else:
        print("Invalid input! Please try again")

    print("\nChoose a menu for Sunday")
    print("\nFor breakfast:")
    print("1.", xb1.description)
    print("2.", xb2.description)
    print("\nFor lunch:")
    print("1.", xl1.description)
    print("2.", xl2.description)
    print("\nFor dinner:")
    print("1.", xd1.description)
    print("2.", xd2.description)
    while True:
        selectionlist = ['1 1 1', '1 1 2', '1 2 1', '1 2 2', '2 1 1', '2 1 2', '2 2 1', '2 2 2']
        selection_sunday = input("\nChoose one option from each meal (breakfast, lunch, dinner)"
                                 "\nand enter each number with a space(ex:1 2 1): ")
        if selection_sunday in selectionlist:
            break
        else:
            print("\nInvalid input! Please try again")
    else:
        print("Invalid input! Please try again")

    b, l, d = selection_monday.split()
    print("\nFor Monday you chose:")
    if b == "1":
        print(mb1.description)
    elif b == "2":
        print(mb2.description)
    if l == "1":
        print(ml1.description)
    elif l == "2":
        print(ml2.description)
    if d == "1":
        print(md1.description)
    elif d == "2":
        print(md2.description)

    print("\nFor Tuesday you chose:")
    b, l, d = selection_tuesday.split()
    if b == "1":
        print(tb1.description)
    elif b == "2":
        print(tb2.description)
    if l == "1":
        print(tl1.description)
    elif l == "2":
        print(tl2.description)
    if d == "1":
        print(td1.description)
    elif d == "2":
        print(td2.description)

    print("\nFor Wednesday you chose:")
    b, l, d = selection_wednesday.split()
    if b == "1":
        print(wb1.description)
    elif b == "2":
        print(wb2.description)
    if l == "1":
        print(wl1.description)
    elif l == "2":
        print(wl2.description)
    if d == "1":
        print(wd1.description)
    elif d == "2":
        print(wd2.description)

    print("\nFor Thursday you chose:")
    b, l, d = selection_thursday.split()
    if b == "1":
        print(thb1.description)
    elif b == "2":
        print(thb2.description)
    if l == "1":
        print(thl1.description)
    elif l == "2":
        print(thl2.description)
    if d == "1":
        print(thd1.description)
    elif d == "2":
        print(thd2.description)

    print("\nFor Friday you chose:")
    b, l, d = selection_friday.split()
    if b == "1":
        print(fb1.description)
    elif b == "2":
        print(fb2.description)
    if l == "1":
        print(fl1.description)
    elif l == "2":
        print(fl2.description)
    if d == "1":
        print(fd1.description)
    elif d == "2":
        print(fd2.description)

    print("\nFor Saturday you chose:")
    b, l, d = selection_saturday.split()
    if b == "1":
        print(sb1.description)
    elif b == "2":
        print(sb2.description)
    if l == "1":
        print(sl1.description)
    elif l == "2":
        print(sl2.description)
    if d == "1":
        print(sd1.description)
    elif d == "2":
        print(sd2.description)

    print("\nFor Sunday you chose:")
    b, l, d = selection_sunday.split()
    if b == "1":
        print(xb1.description)
    elif b == "2":
        print(xb2.description)
    if l == "1":
        print(xl1.description)
    elif l == "2":
        print(xl2.description)
    if d == "1":
        print(xd1.description)
    elif d == "2":
        print(xd2.description)
    print("\nYour order is ready to be shipped to your closest food locker!")


def vegandaily():
    try:
        while True:
            day_of_week = input("\nPlease enter what weekday would you like to receive your menu: ")
            if day_of_week == "monday":
                print("Your menu for", day_of_week, "is: ")
                print("\nFor breakfast:")
                print("1.", mb2.description)
                print("\nFor lunch:")
                print("1.", ml2.description)
                print("\nFor dinner:")
                print("1.", md2.description)
                break
            elif day_of_week == "tuesday":
                print("Your menu for", day_of_week, "is: ")
                print("\nFor breakfast:")
                print("1.", tb2.description)
                print("\nFor lunch:")
                print("1.", tl2.description)
                print("\nFor dinner:")
                print("1.", td2.description)
                break
            elif day_of_week == "wednesday":
                print("Your menu for", day_of_week, "is: ")
                print("\nFor breakfast:")
                print("1.", wb2.description)
                print("\nFor lunch:")
                print("1.", wl2.description)
                print("\nFor dinner:")
                print("1.", wd2.description)
                break
            elif day_of_week == "thursday":
                print("Your menu for", day_of_week, "is: ")
                print("\nFor breakfast:")
                print("1.", thb2.description)
                print("\nFor lunch:")
                print("1.", thl2.description)
                print("\nFor dinner:")
                print("1.", thd2.description)
                break
            elif day_of_week == "friday":
                print("Your menu for", day_of_week, "is: ")
                print("\nFor breakfast:")
                print("1.", fb2.description)
                print("\nFor lunch:")
                print("1.", fl2.description)
                print("\nFor dinner:")
                print("1.", fd2.description)
                break
            elif day_of_week == "saturday":
                print("Your menu for", day_of_week, "is: ")
                print("\nFor breakfast:")
                print("1.", sb2.description)
                print("\nFor lunch:")
                print("1.", sl2.description)
                print("\nFor dinner:")
                print("1.", sd2.description)
                break
            elif day_of_week == "sunday":
                print("Your menu for", day_of_week, "is: ")
                print("\nFor breakfast:")
                print("1.", xb2.description)
                print("\nFor lunch:")
                print("1.", xl2.description)
                print("\nFor dinner:")
                print("2.", xd2.description)
                break
            else:
                print("Invalid input! Please try again.")
    except:
        print("There was an error! Please try again.")

    print("\nYour order is ready to be shipped to your closest food locker!")


def veganweekly():
    print("Your menu is: ")
    print("\nMonday")
    print("For breakfast:")
    print("1.", mb2.description)
    print("For lunch:")
    print("1.", ml2.description)
    print("For dinner:")
    print("1.", md2.description)

    print("\nTuesday")
    print("For breakfast:")
    print("1.", tb2.description)
    print("For lunch:")
    print("1.", tl2.description)
    print("For dinner:")
    print("1.", td2.description)

    print("\nWednesday")
    print("For breakfast:")
    print("1.", wb2.description)
    print("For lunch:")
    print("1.", wl2.description)
    print("For dinner:")
    print("1.", wd2.description)

    print("\nThursday")
    print("For breakfast:")
    print("1.", thb2.description)
    print("For lunch:")
    print("1.", thl2.description)
    print("For dinner:")
    print("1.", thd2.description)

    print("\nFriday")
    print("For breakfast:")
    print("1.", fb2.description)
    print("For lunch:")
    print("1.", fl2.description)
    print("For dinner:")
    print("1.", fd2.description)

    print("\nSaturday")
    print("For breakfast:")
    print("1.", sb2.description)
    print("For lunch:")
    print("1.", sl2.description)
    print("For dinner:")
    print("1.", sd2.description)

    print("\nSunday")
    print("For breakfast:")
    print("1.", xb2.description)
    print("For lunch:")
    print("1.", xl2.description)
    print("For dinner:")
    print("1.", xd2.description)
    print("\nYour order is ready to be shipped to your closest food locker!")


def main_user():
    # welcome the user
    print("Welcome to Global Food Solutions! We are a startup in the food industry that serves 3 menus a day from monday-friday.")
    # introduce types of subscription
    print("Before getting started, it is important to know that we offer 2 types of subscriptions!")
    print("1. Daily subscription (15€)" "\n2. Weekly subscription (70€)")
    while True:
        type_subscription = input("\nWhat subscription would you like to choose? (1 or 2): ")
        if type_subscription == '1' or type_subscription == '2':
            break
        else:
            print("\nInvalid input! Please try again.")

    while True:
        vegan = input("\nAre you vegan?(yes or no)? ")
        vegan = vegan.lower()
        if vegan == 'yes' or vegan == 'no':
            if vegan == "no":
                while True:
                    if type_subscription == "1":
                        return daily()
                        break
                    elif type_subscription == "2":
                        return weekly()
                        break
                    else:
                        print("Please enter a valid number (1 or 2)")
                        break

            elif vegan == "yes":
                while True:
                    if type_subscription == "1":
                        return vegandaily()
                        break
                    elif type_subscription == "2":
                        return veganweekly()
                        break
                    else:
                        print("Please enter a valid number (1 or 2)")
                        break
        else:
            print("\nInvalid input! Please try again.")

def delivery():
    class Edge():
        def __init__(self, weight, startVertex, targetVertex):
            self.weight = weight
            self.startVertex = startVertex
            self.targetVertex = targetVertex

    class Node():
        def __init__(self, name):
            self.name = name
            self.visited = False
            self.adjacencyList = []
            self.minDistance = float("inf")
            self.predecessor = None

        def __lt__(self, other):
            selfPriority = self.minDistance
            otherPriority = other.minDistance
            return selfPriority < otherPriority

        def calculateShortestPath(self):
            q = []
            startVertex = self
            startVertex.minDistance = 0
            heapq.heappush(q, (startVertex.minDistance, startVertex))
            while q:
                currentVertex = heapq.heappop(q)[1]
                for edge in currentVertex.adjacencyList:
                    u = edge.startVertex
                    v = edge.targetVertex
                    newDistance = u.minDistance + edge.weight
                    if newDistance < v.minDistance:
                        v.predecessor = u
                        v.minDistance = newDistance
                        heapq.heappush(q, (v.minDistance, v))

        def getShortestPathTo(self, targetVertex):
            print("shortest path to vertex is:", targetVertex.minDistance)
            node = targetVertex
            path = []
            while node is not None:
                path.append(node.name)
                node = node.predecessor
            path.reverse()
            return path

    nodeA = Node("Calle de Daoiz")
    nodeB = Node("Calle del Cardenal Zuñiga")
    nodeC = Node("Calle de Velarde")
    nodeD = Node("Plaza Mayor")
    nodeE = Node("Calle del Soldado Español")
    nodeF = Node("Calle de las Nieves")
    nodeG = Node("Calle de Riaza")
    nodeH = Node("Calle de los Vargas")
    nodeI = Node("Calle Rosario")
    nodeJ = Node("Calle Jeromino de Aliaga")
    nodeK = Node("Calle de Maria Zambrano")
    nodeL = Node("Calle de Colon")
    nodeM = Node("Calle Santa Catalina")
    nodeN = Node("Calle Ceullar")

    edge1 = Edge(1.06, nodeA, nodeB)
    edge2 = Edge(0.04, nodeA, nodeC)
    edge3 = Edge(1.17, nodeB, nodeE)
    edge4 = Edge(1.85, nodeB, nodeG)
    edge5 = Edge(0.56, nodeC, nodeD)
    edge6 = Edge(0.52, nodeC, nodeK)
    edge7 = Edge(1.47, nodeC, nodeB)
    edge8 = Edge(0.50, nodeD, nodeA)
    edge9 = Edge(0.17, nodeD, nodeK)
    edge10 = Edge(0.75, nodeD, nodeL)
    edge11 = Edge(1.02, nodeE, nodeG)
    edge12 = Edge(1.81, nodeF, nodeE)
    edge13 = Edge(0.59, nodeG, nodeF)
    edge14 = Edge(0.60, nodeG, nodeH)
    edge15 = Edge(0.27, nodeH, nodeM)
    edge16 = Edge(1.22, nodeH, nodeI)
    edge17 = Edge(0.48, nodeI, nodeF)
    edge18 = Edge(0.14, nodeJ, nodeH)
    edge19 = Edge(1.06, nodeK, nodeJ)
    edge20 = Edge(0.19, nodeL, nodeK)
    edge21 = Edge(1.43, nodeM, nodeL)
    edge22 = Edge(0.73, nodeM, nodeN)
    edge23 = Edge(1.03, nodeN, nodeI)

    nodeA.adjacencyList = [edge1, edge2]
    nodeB.adjacencyList = [edge3, edge4]
    nodeC.adjacencyList = [edge5, edge6, edge7]
    nodeD.adjacencyList = [edge8, edge9, edge10]
    nodeE.adjacencyList = [edge11]
    nodeF.adjacencyList = [edge12]
    nodeG.adjacencyList = [edge13, edge14]
    nodeH.adjacencyList = [edge15, edge16]
    nodeI.adjacencyList = [edge17]
    nodeJ.adjacencyList = [edge18]
    nodeK.adjacencyList = [edge19]
    nodeL.adjacencyList = [edge20]
    nodeM.adjacencyList = [edge21, edge22]
    nodeN.adjacencyList = [edge23]

    print("Calle Daoiz \n "
          "Calle del Cardenal Zuñiga \n "
          "Calle de Velarde \n "
          "Plaza Mayor \n "
          "Calle del Soldado español \n "
          "Calle de las nieves \n "
          "Calle de Riaza \n "
          "Calle de los vargas \n "
          "Calle Rosario \n "
          "Calle Jeronimo de Aliaga \n "
          "Calle de Maria Zambrano \n "
          "Calle de Colon \n "
          "Calle Santa Catalina \n "
          "Calle Ceulla")

    while True:
        closest_location = input("\nWhat is your closest location? ")
        if closest_location == "Calle de Daoiz":
            closest_location = nodeA
            break
        if closest_location == "Calle del Cardenal Zuñiga":
            closest_location = nodeB
            break
        if closest_location == "Calle de Velarde":
            closest_location = nodeC
            break
        if closest_location == "Plaza Mayor":
            closest_location = nodeD
            break
        if closest_location == "Calle del Soldado español":
            closest_location = nodeE
            break
        if closest_location == "Calle de las nieves":
            closest_location = nodeF
            break
        if closest_location == "Calle de Riaza":
            closest_location = nodeG
            break
        if closest_location == "Calle de los vargas":
            closest_location = nodeH
            break
        if closest_location == "Calle Rosario":
            closest_location = nodeI
            break
        if closest_location == "Calle Jeronimo de Aliaga":
            closest_location = nodeJ
            break
        if closest_location == "Calle de Maria Zambrano":
            closest_location = nodeK
            break
        if closest_location == "Calle de Colon":
            closest_location = nodeL
            break
        if closest_location == "Calle Santa Catalina":
            closest_location = nodeM
            break
        if closest_location == "Calle Ceulla":
            closest_location = nodeN
            break
        else:
            print("\nPlease write one of the locations above respecting Otrography and Capital letters, also no space at the end")

    while True:
        final_location = input("\nWhere do you want to go? ")
        if final_location == "Calle de Daoiz":
            final_location = nodeA
            break
        if final_location == "Calle del Cardenal Zuñiga":
            final_location = nodeB
            break
        if final_location == "Calle de Velarde":
            final_location = nodeC
            break
        if final_location == "Plaza Mayor":
            final_location = nodeD
            break
        if final_location == "Calle del Soldado español":
            final_location = nodeE
            break
        if final_location == "Calle de las nieves":
            final_location = nodeF
            break
        if final_location == "Calle de Riaza":
            final_location = nodeG
            break
        if final_location == "Calle de los vargas":
            final_location = nodeH
            break
        if final_location == "Calle Rosario":
            final_location = nodeI
            break
        if final_location == "Calle Jeronimo de Aliaga":
            final_location = nodeJ
            break
        if final_location == "Calle de Maria Zambrano":
            final_location = nodeK
            break
        if final_location == "Calle de Colon":
            final_location = nodeL
            break
        if final_location == "Calle Santa Catalina":
            final_location = nodeM
            break
        if final_location == "Calle Ceulla":
            final_location = nodeN
            break
        else:
            print("\nPlease write one of the locations above respecting Otrography and Capital letters, also no space at the end")

    closest_location.calculateShortestPath()
    xy = closest_location.getShortestPathTo(final_location)
    print(xy)

def main():

    while True:
        choice = input("Are you a delivery man (1) or a user (2)? ")
        if choice == '2':
            return main_user()
        elif choice == '1':
            return delivery()

main()