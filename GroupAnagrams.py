#T: O(nmlogm) S: O(n+m)
def groupAnagrams(strs):
        hm = {}
        for x in strs:
            sorted_x = "".join(sorted(x))
            if sorted_x not in hm.keys():
                hm[sorted_x] = [x]
            else:
                hm[sorted_x].append(x)
        res = []
        for x in hm:
            res.append(hm[x])
        return res


