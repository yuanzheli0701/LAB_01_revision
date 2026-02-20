import sys

m = "URGENT Message!!! HHHHHeey"
u = 0
p = 0
tl = 0  
s = False
rc = 1
prev = None

for c in m:
    if c.isupper():
        u += 1
        tl += 1
    elif c.islower():
        tl += 1
    if c == '!' or c == '?':
        p += 1
    if c == prev:
        rc += 1
    else:
        rc = 1
    if rc > 3:
        s = True
    prev = c

if tl > 0:
    cr = u / tl
else:
    cr = 0
lbl = ""

if (cr >= 0.6) or (p >= 5):
    lbl = "AGGRESSIVE"
elif (cr >= 0.3) or (p >= 3):
    lbl = "URGENT"
else:
    lbl = "CALM"

print("letter style: " + lbl)
print("it's spam? " + str(s))