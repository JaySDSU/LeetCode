class Solution:
	def searchList(self, nums : List[int], target:int) -> int:
        if not nums:
            return -1
        start = 0
        end = len(nums)-1
        
        while start<=end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            
            if nums[start]<=nums[mid]:
                if nums[start] <= target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] <= target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        
        return -1
        
obj1 = Solution()
a1 = [4,5,6,7,0,1,2,3]
target = 0
print(obj1.searchList(a1,target))