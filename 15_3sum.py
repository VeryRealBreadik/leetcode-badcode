from typing import List


class Solution:
    # def threeSum(self, nums: List[int]) -> List[List[int]]: # Brute force solution
    #     triplets = []
    #     for i in range(len(nums) - 2):
    #         for j in range(i + 1, len(nums) - 1):
    #             for z in range(j + 1, len(nums)):
    #                 triplet = sorted([nums[i], nums[j], nums[z]])
    #                 if sum(triplet) == 0 and triplet not in triplets:
    #                     triplets.append(triplet)
        
    #     return triplets
    
    def threeSum(self, nums: List[int]) -> List[List[int]]: # Two pointers solution
        nums.sort()
        triplets = []
        nums_len = len(nums)
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left_pointer = i + 1
            right_pointer = nums_len - 1
            while left_pointer < right_pointer:
                triplet = [nums[i], nums[left_pointer], nums[right_pointer]]
                triplet_sum = sum(triplet)
                if triplet_sum == 0:
                    triplets.append(triplet)
                    left_pointer += 1
                    
                    while nums[left_pointer] == nums[left_pointer - 1] and left_pointer < right_pointer:
                        left_pointer += 1
                elif triplet_sum < 0:
                    left_pointer += 1
                elif triplet_sum > 0:
                    right_pointer -= 1
        
        return triplets

def main():
    solution = Solution()
    nums1 = [-1, 0, 1, 2, -1, -4]
    nums2 = [0, 1, 1]
    nums3 = [0, 0, 0]
    result1 = solution.threeSum(nums1)
    result2 = solution.threeSum(nums2)
    result3 = solution.threeSum(nums3)
    print(f"{nums1}: {result1}")
    print(f"{nums2}: {result2}")
    print(f"{nums3}: {result3}")


if __name__ == "__main__":
    main()
