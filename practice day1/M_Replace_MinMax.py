a = input()
nums = list(map(int, input().split()))


x = max(nums)
y = min(nums)

for i in range(len(nums)):
    if nums[i] == x:
        nums[i] = y
    elif nums[i] == y:
        nums[i] = x

for a in nums:
    print(a,end=" ")