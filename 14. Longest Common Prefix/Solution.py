class Solution:
    def longestCommonPrefix(self, strs):

        pre = min(strs, key=len)

        for i in strs:
            while not i.startswith(pre):
                pre = pre[:-1]

        return pre

    """
    if not strs:
        return ""

    shortest = min(strs, key=len)
    for i, char in enumerate(shortest):
        for other in strs:
            if other[i] != char:
                return shortest[:i]

    return shortest
    """