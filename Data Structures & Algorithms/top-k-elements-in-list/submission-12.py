class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n_count = {}
        for n in nums:
            n_count[n] = n_count.get(n, 0) + 1
        n_sort = sorted(n_count.items(), key = lambda x: x[1], reverse = True)
        return [num[0] for num in n_sort[0:k]]
     
