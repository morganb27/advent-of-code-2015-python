import hashlib

PUZZLE = "ckczppom"

PART_1, PART_2 = None, None

for i in range(10000000):
    current = PUZZLE + str(i)
    hash = hashlib.md5(current.encode("utf-8")).hexdigest()
    if hash[:5] == "00000":
        PART_1 = current[8:] if PART_1 == None else PART_1
    if hash[:6] == "000000":
        PART_2 = current[8:]
        break

print(PART_1)
print(PART_2)