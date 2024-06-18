#T: O(n) S: O(n)
def containsDuplicate(nums):
        return len(nums) != len(set(nums))