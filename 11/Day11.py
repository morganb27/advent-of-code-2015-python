PASSWORD = "hxbxwxba"

def find_new_password():
    global PASSWORD
    for _ in range(2):
        while True:
            PASSWORD = next_password(PASSWORD)
            if isPasswordValid(PASSWORD):
                print(f"Next password is: {PASSWORD}")
                break

def next_password(p):
    if p == 'z':
        return 'a'
    if p[-1] == 'z':
        return next_password(p[:-1]) + 'a'
    return p[:-1] + chr(ord(p[-1]) + 1)

def isPasswordValid(s):
    FORBIDDEN = ["i", "o", "l"]
    straight = False
    pairs = set()
    if any(x in s for x in FORBIDDEN):
        return False
    for i in range(len(s) - 2):
        if ord(s[i]) == ord(s[i+1]) - 1 == ord(s[i+2]) - 2:
            straight = True
        if s[i] == s[i+1]:
            pairs.add((s[i], s[i+1]))
    if s[-1] == s[-2]:
        pairs.add((s[-1], s[-2]))
    return straight and len(pairs) >= 2

find_new_password()