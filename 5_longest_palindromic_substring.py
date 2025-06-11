class Solution(object):
    def longestPalindrome(self, s: str) -> str:
        longest_substring = s[0]
        for substring_center in range(len(s) - 1):
            left_pointer = substring_center - 1
            right_pointer = substring_center + 1
            longest_odd_substring = self.check_for_palindrome(s, left_pointer, right_pointer)
            
            left_pointer = substring_center
            right_pointer = substring_center + 1
            longest_even_substring = self.check_for_palindrome(s, left_pointer, right_pointer)
            
            if len(longest_substring) < len(longest_odd_substring):
                longest_substring = longest_odd_substring
            if len(longest_substring) < len(longest_even_substring):
                longest_substring = longest_even_substring
        return longest_substring
    
    def check_for_palindrome(self, s: str, left_pointer: int, right_pointer: int) -> str: 
        while left_pointer >= 0 and right_pointer <= len(s) - 1:
            if s[left_pointer] != s[right_pointer]:
                break
            left_pointer -= 1
            right_pointer += 1
        
        return s[left_pointer + 1:right_pointer]

def main():
    solution = Solution()
    s1 = "babaasdwqqwoejqwejqjjjiiijjjd"
    s2 = "a"
    result1 = solution.longestPalindrome(s1)
    result2 = solution.longestPalindrome(s2)
    print(f"{s1}: {result1}")
    print(f"{s2}: {result2}")


if __name__ == "__main__":
    main()
