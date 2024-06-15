def topKFrequent(nums, k):
        hm = {}
        for x in list(set(nums)):
            count = nums.count(x)
            if count not in hm:
                hm[count] = [x]
            else:
                hm[count].append(x)
        res = []
        for i in range(len(nums), -1, -1):
            if k == 0:
                return res
            elif i in hm:
                res += hm[i]
                k -= len(hm[i])