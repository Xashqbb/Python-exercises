class Solution(object):
    def jump(self,nums):
        end = 0
        farthest = 0
        jumps = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == end:
                end = farthest
                jumps += 1
        return jumps
"""""
    def jump(self, nums):
       count=0
       j=nums[0]
       for i in range(len(nums)):
           if nums[i+j]!=nums[len(nums)-1]:
               count+=1
           elif j>=nums[i]:
               return count

       return count
"""""