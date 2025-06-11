class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        reversed_x = self.reverse(x)
        if x == reversed_x:
            return True
        return False
    
    def reverse(self, x: int) -> int:
        reversed_x = 0
        
        while x > 0:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10

        return reversed_x
        
def main():
    solution = Solution()
    x1 = 121
    x2 = -121
    x3 = 10
    result1 = solution.isPalindrome(x1)
    result2 = solution.isPalindrome(x2)
    result3 = solution.isPalindrome(x3)
    print(f"{x1}: {result1}")
    print(f"{x2}: {result2}")
    print(f"{x3}: {result3}")


if __name__ == "__main__":
    main()
