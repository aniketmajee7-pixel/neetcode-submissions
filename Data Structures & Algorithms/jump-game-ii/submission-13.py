class Solution:
    def jump(self, nums: List[int]) -> int:
        counter=1
        size=len(nums)
        if size==1:
            return 0
        max_reach=0
        index=0
        i=0
        while(i+nums[i]<size-1):
            max_reach=nums[i]+i
            index=i
            for j in range(nums[i]):
                k=i+j+1
                if nums[k]+k>max_reach:
                    max_reach=nums[k]+k
                    index=k
            counter+=1
            i=index
        return counter



