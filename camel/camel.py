def main():
    words = input("camelCase: ")
    convert(words)

def convert(words):
    if words.islower():
        print(words)
    else:
        for i in range(len(words)):
            if words[i].isupper():
                upper = words[i]
                lower = "_" + upper.casefold()
                words = words.replace(upper, lower)
        print(words)

main()