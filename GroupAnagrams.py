def groupAnagrams(strs):
    hm = {sorted(x):x for x in strs}
    print(hm)


groupAnagrams(["eat","tea","tan","ate","nat","bat"])