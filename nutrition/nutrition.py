def main():
    item = input("Item: ").casefold()
    fruit(item)

def fruit(item):
    match item:
        case "apple":
            print("Calories: 130")
        case "avocado" | "cantaloupe" | "pineapple":
            print("Calories: 50")
        case "banana":
            print("Calories: 110")
        case "grapefruit" | "nectarine" | "peach":
            print("Calories: 60")
        case "grapes" | "kiwifruit":
            print("Calories: 90")
        case "lemon":
            print("Calories: 15")
        case "lime":
            print("Calories: 20")
        case "orange":
            print("Calories: 80")
        case "pear" | "sweet cherries":
            print("Calories: 100")
        case "plums":
            print("Calories: 70")
        case _:
            print("")

main()