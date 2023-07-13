class Solution(object):
    def lengthOfLastWord(self, s):
        k=s.split()
        n=k[-1]
        return len(n)