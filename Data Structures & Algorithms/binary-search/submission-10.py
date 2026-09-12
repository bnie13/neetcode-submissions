class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while nums[low] != target and nums[high] != target:
            middle = (high + low) // 2
            if middle == high or middle == low:
                return -1
            if nums[middle] == target:
                return middle
            if nums[middle] > target:
                high = middle
            if nums[middle] < target:
                low = middle
        if nums[low] == target:
            return low
        return high

            
        




        