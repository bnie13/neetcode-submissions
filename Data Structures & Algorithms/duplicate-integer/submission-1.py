class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for n in nums:
            if n in seen:
                return True
            else:
                seen[n] = 1
        return False
            

        def main():
            nums = [1,2,3,3]
            b = hasDuplicate(nums)
            print(b)

        if __name__ == "__main__":
            main()