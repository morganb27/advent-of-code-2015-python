PUZZLE = [line.strip() for line in open("input.txt")]

PART_1, PART_2 = 0, 0

for line in PUZZLE:
    l, w, h = map(int, line.split("x"))
    min_area = min(l+w, w+h, h+l)
    area = 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
    PART_2 += 2*min_area + l*w*h
    PART_1 += area

print(PART_1)
print(PART_2)