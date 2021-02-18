a = int(input())
b = input()
x = b.split(" ")
c = map(int, x)
temps = 0
for i in c:
    if i < 0:
        temps += 1
print(temps)
