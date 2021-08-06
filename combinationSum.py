# we pass currentSum path, remaining value to target(considering current value) and index to helper function

from typing import List
class Solution:
    def combinationSum(self, candidates : List[int], target: int) -> List[List[int]]:
        combinations = []
        
        def helper(remaining, current_sum , index):
            if remaining == 0:
                combinations.append(current_sum)
                return
            
            for i in range(index,len(candidates)):
                if candidates[i] > remaining:
                    break
                helper(remaining-candidates[i], current_sum + [candidates[i]], i) 
        candidates = sorted(candidates)
        helper(target,[],0)
        return combinations
      
obj1 = Solution()
a = [1,2,3,4,6,8]
target = 10
print(obj1.combinationSum(a,target))