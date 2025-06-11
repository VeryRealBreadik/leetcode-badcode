class Solution(object):
    def longestPalindrome(self, s: str) -> str: # Fix this
        """
        :type s: str
        :rtype: str
        """
        left_pointer = 0
        max_len = 1
        for right_pointer in range(1, len(s)):
            if right_pointer <= left_pointer:
                continue
            for i in range(left_pointer, right_pointer + 1):
                if s[i] != s[right_pointer - left_pointer]:
                    left_pointer += 1
                    break
            max_len = max(max_len, right_pointer - left_pointer + 1)
        return max_len

def main():
    solution = Solution()
    s1 = "babad"
    s2 = "cbbd"
    result1 = solution.longestPalindrome(s1)
    result2 = solution.longestPalindrome(s2)
    print(result1)
    print(result2)


if __name__ == "__main__":
    main()
