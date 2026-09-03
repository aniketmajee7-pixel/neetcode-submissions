class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        length=len(nums)
        def min_heap(length,root_idx):
            while True:
                smallest=root_idx
                left=2*root_idx+1
                right=2*root_idx+2
                if left<length and nums[left]<nums[smallest]:
                    smallest=left
                if right<length and nums[right]<nums[smallest]:
                    smallest=right
                if smallest!=root_idx:
                    nums[root_idx],nums[smallest]=nums[smallest],nums[root_idx]
                    root_idx=smallest
                else:break
        for i in range(length//2-1,-1,-1):
            min_heap(length,i)
        res=[]
        for i in range(length):
            res.append(nums[0])
            nums[0]=nums[len(nums)-1-i]
            min_heap(length-1-i,0)

        return res


        
        