from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        nums_len = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]
        for i in range(nums_len):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left_pointer = i + 1
            right_pointer = nums_len - 1
            while left_pointer < right_pointer:
                triplet_sum = nums[i] + nums[left_pointer] + nums[right_pointer]
                if triplet_sum == target:
                    closest_sum = triplet_sum
                    return closest_sum
                
                if abs(target - closest_sum) > abs(target - triplet_sum):
                    closest_sum = triplet_sum

                if triplet_sum > target:
                    right_pointer -= 1
                elif triplet_sum < target:
                    left_pointer += 1
        
        return closest_sum

def main():
    solution = Solution()
    nums1 = [10,20,30,40,50,60,70,80,90]
    nums2 = [0, 1, 2]
    target1 = 1
    target2 = 3
    result1 = solution.threeSumClosest(nums1, target1)
    result2 = solution.threeSumClosest(nums2, target2)
    print(f"{nums1}: {result1}")
    print(f"{nums2}: {result2}")


if __name__ == "__main__":
    main()
