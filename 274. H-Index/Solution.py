class Solution(object):
    def hIndex(self, citations):
        citations.sort(reverse=True)

        h_index = 0

        for i, c in enumerate(citations):
            if c >= i + 1:
                h_index += 1
            else:
                break

        return h_index