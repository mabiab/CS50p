def main():
    phrase = input("Input: ")
    word = ""

    for i in range(len(phrase)):
        if not(phrase[i] == 'a' or phrase[i] == 'A' or phrase[i] == 'e' or phrase[i] == 'E' or phrase[i] == 'i' or phrase[i] == 'I' or phrase[i] == 'o' or phrase[i] == 'O' or phrase[i] == 'u' or phrase[i] == 'U'):
            word += phrase[i]
    print(word)

main()