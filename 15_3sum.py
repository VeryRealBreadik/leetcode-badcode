from typing import List


class Solution:
    # def threeSum(self, nums: List[int]) -> List[List[int]]: # Brute force
    #     triplets = []
    #     for i in range(len(nums) - 2):
    #         for j in range(i + 1, len(nums) - 1):
    #             for z in range(j + 1, len(nums)):
    #                 triplet = sorted([nums[i], nums[j], nums[z]])
    #                 if sum(triplet) == 0 and triplet not in triplets:
    #                     triplets.append(triplet)
        
    #     return triplets
    
    def threeSum(self, nums: List[int]) -> List[List[int]]: # simplifying to a two sum problem
        triplets = []
        nums_dict = {}
        for i in range(len(nums) - 1):
            nums_dict[i] = nums[i]
            target = 0 - nums[i]
            for j in range(i + 1, len(nums)):
                remainder = target - nums[j]
                triplet = sorted([nums[i], nums[j], remainder])
                if remainder in nums_dict and triplet not in triplets: # FIXME: Do something about duplicate usage of a num
                    triplets.append(triplet)
                nums_dict[nums[j]] = j
        
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
