from collections import Counter

class Solution:
    def topKFrequent(self, words, k):
        count = Counter(words)

        result = sorted(count, key=lambda x: (-count[x], x))

        return result[:k]