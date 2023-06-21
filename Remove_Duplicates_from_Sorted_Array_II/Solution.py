class Solution(object):
    def removeDuplicates(self,nums):
        if len(nums) <= 2:
            return len(nums)
        count = 1
        pos = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1

            if count <= 2:
                nums[pos] = nums[i]
                pos += 1
        print(nums[:pos])
        return pos