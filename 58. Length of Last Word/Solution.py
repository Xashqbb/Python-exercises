class Solution(object):
    def lengthOfLastWord(self, s):
        k=s.split()
        return len(k[-1])