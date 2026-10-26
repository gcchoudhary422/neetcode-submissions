class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out = []
        # frequencies = Counter(nums)
        frequencies = {}
        for num in nums:
            frequencies[num] = 1 + frequencies.get(num,0)
        bucket = [[] for i in range(len(nums)+1)]
        for num, count in frequencies.items():
            bucket[count].append(num)
        for i in range(len(bucket)-1, 0, -1):
            for j in bucket[i]:
              out.append(j)
              if len(out) == k:
                return out