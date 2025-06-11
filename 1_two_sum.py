class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> tuple:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in nums_dict:
                return nums_dict[remainder], i
            nums_dict[nums[i]] = i

def main():
    solution = Solution()
    result = solution.twoSum([3, 3], 6)
    print(result)


if __name__ == "__main__":
    main()
