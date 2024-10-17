def all_even(b):
    for i in range(len(b)):
        if b[i] % 2 != 0:
            return False
    return True

def operation(b):
    for i in range(len(b)):
        b[i] = b[i] // 2 

n = int(input())
b = list(map(int, input().split()))

ans = 0
while all_even(b):
    ans += 1
    operation(b)

print(ans)
