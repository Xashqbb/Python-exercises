from Solution import Solution
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
sol=Solution()

output=sol.fullJustify(words,maxWidth)
for line in output:
    print(line)
