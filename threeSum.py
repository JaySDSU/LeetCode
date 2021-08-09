# left and right pointer for every element in array
# will increase left and right pointer if the values of next number are same when we found a result
# will also increase the current index if its the same value as of the last one.

def threeSum(nums):
    nums.sort()
    result = []
    
    for i in range(len(nums)-2):
        left = i+1
        right = len(nums) - 1
        if i > 0 and nums[i] == nums[i-1]:
            continue
        while left < right:
            summ = nums[i] + nums[left] + nums[right]
            
            if summ == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left<right and nums[left] == nums[left+1]:
                    left = left + 1
                while left<right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
            
            elif summ > 0:
                right -= 1
            else:
                left += 1
    
    return result

n1 = [-1,0,1,2,-1,-4]

print(threeSum(n1))
