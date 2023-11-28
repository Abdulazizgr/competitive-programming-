
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

l = len(nums)
first = nums[:-k+1]
last = nums[k+1:]
nums[:l-k] = last
nums[l-k:] = first
print(nums)
