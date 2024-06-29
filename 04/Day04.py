import hashlib

SECRET_KEY = "ckczppom"
HASH1 = None
HASH2 = None

def md5():
    i = 1
    while True:
        s = SECRET_KEY + str(i)
        global HASH1, HASH2
        h = hashlib.md5(s.encode()).hexdigest()
        if h[:5] == "00000" and HASH1 is None:
            HASH1 = s[8:]
        if h[:6] == "000000":
            HASH2 = s[8:]
            break
        i+=1
    print(f"Solution for part 1 is: {HASH1}")
    print(f"Solution for part 2 is: {HASH2}")

md5()
