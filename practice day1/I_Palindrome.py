a = input()
c = a
b = c[::-1]

b = b.lstrip('0')

print(b)
if a == b:
    print("YES")
else:
    print("NO")
