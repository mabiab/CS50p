def main():
    total = 0
    change = int(input("Amount due: 50\n"))

    while (total < 50):
        if change == 25 or change == 10 or change == 5:
            total += change
            if total == 50:
                print("Change owed: 0")
                break
            else:
                if total >= 50:
                    change = total - 50
                    print("Change owed: "+str(change))
                else:
                    change = int(input("Amount due: " + str(50-total)))
        else:
            print("Amount due: 50")

main()