PASSWORD = "hxbxwxba"

def next_password(p):
    if p == "z":
        return "a"
    if p[-1] == "z":
        return next_password(p[:-1]) + "a"
    return p[:-1] + chr(ord(p[-1]) + 1)


def is_valid_password(p):
    pairs = set()
    is_increasing = False

    if any(x in "iol" for x in p): 
        return False

    for a, b in zip(p, p[1:]):
        if a == b:
            pairs.add((a, b))

    for i in range(len(p) - 3):
        if ord(p[i]) == ord(p[i+1]) - 1 == ord(p[i+2]) - 2:
            is_increasing = True

    return len(pairs) > 1 and is_increasing




while True:
    PASSWORD = next_password(PASSWORD)
    if is_valid_password(PASSWORD):
        PART_1 = PASSWORD
        break

while True:
    PASSWORD = next_password(PASSWORD)
    if is_valid_password(PASSWORD):
        PART_2 = PASSWORD
        break

    
print(PART_1)
print(PART_2)
