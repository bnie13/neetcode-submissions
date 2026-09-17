class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        start = []
        max_count = 0
        for x in nums_set:
            if not x-1 in nums_set:
                start.append(x)
        for s in start:
            count = 1
            while s+1 in nums_set:
                count += 1
                s += 1
            if count > max_count:
                max_count = count
        return max_count

            


        