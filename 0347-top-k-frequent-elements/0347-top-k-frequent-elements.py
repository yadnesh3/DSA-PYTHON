class Solution:
    def topKFrequent(self, nums, k):
        # Count frequency
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Create buckets
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        # Get k most frequent elements
        result = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result