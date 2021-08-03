# consider base conditions-> there are only two possiblity
# if 1. to rob a house and 2. to not rob house
# want to decide from the maximum amount so
# rob[i] = max(rob[i-2] + currenthouse, rob[i-1])

class Solution:
    def rob(self,nums) -> int:
        prev1 = 0
        prev2 = 0
        
        for i in range(len(nums)):
            temp = prev1
            prev1 = max(prev2 + nums[i], prev1)
            prev2 = temp
        
        return prev1

obj1 = Solution()
a1 = [1,2,3,1]
a2 = [2,7,9,3,1]

print(obj1.rob(a1))
print(obj1.rob(a2))
