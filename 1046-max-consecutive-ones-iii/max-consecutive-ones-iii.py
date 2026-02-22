class Solution(object):
    def longestOnes(self, nums, k):
        l=0
        longest=0
        z=0

        for r in range(len(nums)):

            if nums[r]==0:
                z+=1
            
            while z>k:
                if nums[l]==0:
                    z-=1
                l+=1
            longest=max(longest,r-l+1)
        return longest
        