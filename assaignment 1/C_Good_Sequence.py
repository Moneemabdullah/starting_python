from collections import Counter

n = int(input())
b = list(map(int, input().split()))

array = Counter(b)

ans = 0

for i in array:
    occurrences = array[i]
    if occurrences > i:
        ans += occurrences - i
    elif occurrences < i:
        ans += occurrences

print(ans)
