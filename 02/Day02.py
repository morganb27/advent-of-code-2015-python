import fileinput

DOCUMENT = [line.strip() for line in fileinput.input()]

def wrapping_paper(data):
    res = 0
    for line in data:
        l, w, h = [int(x) for x in line.split('x')]
        minValue = min(min(l*h, l*w), w*h)
        res += 2*l*w + 2*w*h + 2*h*l + minValue
    return res

def ribbon(data):
    res = 0
    for line in data:
        l, w, h = [int(x) for x in line.split('x')]
        x = min(min(l+h, l+w), w+h)
        y = l*w*h
        res += x*2 + y
    return res

print(f"Wrapping paper needed: {wrapping_paper(DOCUMENT)}")
print(f"Total feet of ribbon needed: {ribbon(DOCUMENT)}")