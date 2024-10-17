

a = input()

count_L = 0
count_R = 0
b = []
ans = []

for c in a:
    b.append(c)
    if c == "L":
        count_L += 1
    else:
        count_R += 1
    
    if count_L == count_R:
        ans.append("".join(b))
        b = []
        count_L = 0 
        count_R = 0


print(len(ans))
for X in ans:
    print(X)
