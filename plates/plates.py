def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def minnum(plate):
    for i in range(len(plate)):
        if plate[i].isnumeric():
            return i

def maxnum(plate):
    for i in range(len(plate)-1, 0, -1):
        if plate[i].isnumeric():
            return i

def maxlet(plate):
    for i in range(len(plate)-1, 0, -1):
        if plate[i].isalpha():
            return i

def is_invalid(plate):
    minn = minnum(plate)
    maxn = maxnum(plate)
    maxl = maxlet(plate)
    if minn == None or maxn == None:
        return False
    elif plate[minn] == "0":
        return True
    elif minn < maxl < maxn:
        return True
    else:
        return False

def is_valid(plate):
    for i in range(len(plate)):
        if not(plate[i].isalnum()):
            return False
    if len(plate) > 6 or len(plate) < 2:
        return False
    if plate[0].isnumeric() or plate[1].isnumeric():
        return False
    if is_invalid(plate):
        return False
    else:
        return True

main()