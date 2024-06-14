def twoSum(nums, target):
    hm = dict()
    for i in range(len(nums)):
        if nums[i] in hm:
            return [hm[i], i]
        hm[target - nums[i]] = i

print(twoSum([2,7,11,15], 13))
