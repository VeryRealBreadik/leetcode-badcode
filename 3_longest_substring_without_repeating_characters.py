class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars_dict = {}
        left_pointer = 0
        max_len = 0
        
        for right_pointer, char in enumerate(s):
            if char in chars_dict and chars_dict[char] >= left_pointer:
                left_pointer = chars_dict[char] + 1
            
            max_len = max(max_len, right_pointer - left_pointer + 1)
            chars_dict[char] = right_pointer
        
        return max_len

def main():
    solution = Solution()
    string1 = "abba"
    string2 = "bbbbb"
    string3 = "pwwkew"
    result1 = solution.lengthOfLongestSubstring(string1)
    result2 = solution.lengthOfLongestSubstring(string2)
    result3 = solution.lengthOfLongestSubstring(string3)
    print(f"{string1}: {result1}")
    print(f"{string2}: {result2}")
    print(f"{string3}: {result3}")


if __name__ == "__main__":
    main()
