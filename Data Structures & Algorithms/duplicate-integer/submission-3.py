class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map={}
        for index,number in enumerate(nums):
            if number in hash_map:
                return True
            else:
                hash_map[number]=index
        return False

            