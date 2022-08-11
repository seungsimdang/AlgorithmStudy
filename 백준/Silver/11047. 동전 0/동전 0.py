a, b = input().split()
a = int(a)
b = int(b)
c = []

for i in range(0, int(a)):
    c.append(int(input()))

count = 0

for i in reversed(range(len(c))):
    count += b//c[i]
    b = b % c[i]

print(count)
