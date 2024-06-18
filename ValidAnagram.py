#T: O(nlogn) S: O(n)
def validAnagram(s, t):
    return sorted(s) == sorted(t)
