

nums = [5, 9, 8, 9, 2, 1, 6, 4, 2]
nova = []

if nums[0] >= nums[-1]:
    for num in nums:
        nova.append(nums[0])
else:
    for num in nums:
        nova.append(nums[-1])

print(nova)