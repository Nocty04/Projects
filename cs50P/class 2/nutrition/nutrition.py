def main():
    sobremesa()


def sobremesa():
    fruits = {
        "Apple": 130,
        "Avocado": 50,
        "Banana": 110,
        "Cantaloupe": 50,
        "Grapefruit": 60,
        "Grapes": 90,
        "Honeydew Melon": 50,
        "Kiwifruit": 90,
        "Lemon": 15,
        "Lime": 20,
        "Nectarine": 60,
        "Orange": 80,
        "Peach": 60,
        "Pear": 100,
        "Pineapple": 50,
        "Plums": 70,
        "Strawberries": 50,
        "Sweet Cherries": 100,
        "Tangerine": 50,
        "Watermelon": 80
        }

    fruit = input("what fruit do you want to eat? ").title()
    if fruit not in fruits:
        print("")
    else:
        calories = fruits[fruit]
        print("Calories: ", calories)


main()
#sem title poderia fazer um loop que verificava se o c era supper e se tava na posiçao zero retonava uma boolean
