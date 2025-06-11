class Solution:
    def reverse(self, x: int) -> int:
        negative_multiplier = 1
        if x < 0:
            negative_multiplier = -1
            x *= -1
        reversed_x = 0
        
        while x > 0:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10
        
        if reversed_x >= 2**31:
            return 0
        
        reversed_x *= negative_multiplier
        return reversed_x
        
def main():
    solution = Solution()
    x1 = 123
    x2 = -123
    x3 = 120
    result1 = solution.reverse(x1)
    result2 = solution.reverse(x2)
    result3 = solution.reverse(x3)
    print(f"{x1}: {result1}")
    print(f"{x2}: {result2}")
    print(f"{x3}: {result3}")


if __name__ == "__main__":
    main()
