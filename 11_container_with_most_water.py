from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left_pointer = 0
        right_pointer = len(height) - 1
        while left_pointer < right_pointer:
            width = right_pointer - left_pointer
            if height[left_pointer] < height[right_pointer]:
                min_height = height[left_pointer]
                left_pointer += 1
            else:
                min_height = height[right_pointer]
                right_pointer -= 1
            max_area = max(max_area, min_height * (width))
        
        return max_area
        
def main():
    solution = Solution()
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    height2 = [1, 1]
    result1 = solution.maxArea(height1)
    result2 = solution.maxArea(height2)
    print(f"{height1}: {result1}")
    print(f"{height2}: {result2}")


if __name__ == "__main__":
    main()
