class Solution(object):
    def majorityElement(self, nums):
        if len(nums) < 2:
            return nums[0]
        count = 0
        majElem = 0
        for num in nums:
            if count == 0:
                majElem = num
            count += 1 if num == majElem else -1
        count = 0
        for num in nums:
            if num == majElem:
                count += 1
        if count > len(nums) / 2:
            return majElem
        else:
            return 0