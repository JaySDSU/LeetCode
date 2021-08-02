def twoSum(arr, target):
	dic = {}
	for i in range(len(arr)):
		if target-arr[i] in dic:
			return [dic[target-arr[i]], i]
		else:
			dic[arr[i]] = i
	
	return [-1,-1]

A1 = [2,7,11,15]
a = 9
B1 = [3,2,4]
b = 6
C1 = [3,3]
c = 6

print(twoSum(A1,a))
print(twoSum(B1,b))
print(twoSum(C1,c))