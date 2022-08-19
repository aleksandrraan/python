


def searchInsert(nums:list[int],target:int):
  k=nums
  k.append(target)
  k.sort()
  if len(k)==len(nums):
    return nums.index(target)
  else:
     return k.index(target)
print(searchInsert([1,2],3))