from typing import List


class Solution(object):
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_list = sorted(nums1 + nums2)
        merged_list_len = len(merged_list)
        if len(merged_list) % 2 == 0:
            median = float((merged_list[merged_list_len // 2 - 1] + merged_list[merged_list_len // 2]) / 2)
        else:
            median = float(merged_list[merged_list_len // 2])
        return median

def main():
    solution = Solution()
    nums11 = [1, 3]
    nums12 = [2]
    nums21 = [1, 2]
    nums22 = [3, 4]
    result1 = solution.findMedianSortedArrays(nums11, nums12)
    result2 = solution.findMedianSortedArrays(nums21, nums22)
    print(f"{nums11, nums12}: {result1}")
    print(f"{nums21, nums22}: {result2}")


if __name__ == "__main__":
    main()
