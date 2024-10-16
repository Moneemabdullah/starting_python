a, b = map(int, input().split())

numbers = []

for i in range(a, b + 1):
    str_i = str(i)

    if all(c in '47' for c in str_i):
        numbers.append(str_i)

if len(numbers) == 0:
    print(-1)
else:
    for a in numbers:
        print(a,end =" ") 
print()
