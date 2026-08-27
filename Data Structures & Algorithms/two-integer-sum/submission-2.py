class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={}
        for index,number in enumerate(nums):
            if (target-number) in hash_map:
                return [hash_map[target-number],index]
            else:
                hash_map[number]=index
            
        