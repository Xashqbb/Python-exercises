class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_length = len(words[0])
        word_count = len(words)
        total_length = word_length * word_count

        if len(s) < total_length:
            return []

        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
        result = []
        for i in range(word_length):
            left = i
            word_seen = {}

            for j in range(i, len(s) - word_length + 1, word_length):
                word = s[j: j + word_length]

                if word in word_freq:
                    word_seen[word] = word_seen.get(word, 0) + 1

                    while word_seen[word] > word_freq[word]:
                        word_seen[s[left: left + word_length]] -= 1
                        left += word_length

                    if j + word_length - left == total_length:
                        result.append(left)

                else:
                    word_seen = {}
                    left = j + word_length

        return result