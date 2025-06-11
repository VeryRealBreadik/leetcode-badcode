from typing import List, Tuple


class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> Tuple[int]:
        nums_dict = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in nums_dict:
                return nums_dict[remainder], i
            nums_dict[nums[i]] = i

def main():
    solution = Solution()
    nums1 = [2, 7, 11, 15]
    target1 = 9
    nums2 = [3, 2, 4]
    target2 = 6
    nums3 = [3, 3]
    target3 = 6
    result1 = solution.twoSum(nums1, target1)
    result2 = solution.twoSum(nums2, target2)
    result3 = solution.twoSum(nums3, target3)
    print(f"{nums1, target1}: {result1}")
    print(f"{nums2, target2}: {result2}")
    print(f"{nums3, target3}: {result3}")


if __name__ == "__main__":
    main()
