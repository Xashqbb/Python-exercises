class Solution(object):
    def reverseWords(self, s):

        k=s.split()
        k=k[::-1]
        k= ' '.join(k)
        return k.strip()