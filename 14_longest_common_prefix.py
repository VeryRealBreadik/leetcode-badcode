from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        current_prefix = ""
        for char in strs[0]:
            for string in strs:
                if not string.startswith(current_prefix + char):
                    return current_prefix
            current_prefix += char
        
        return current_prefix
        
def main():
    solution = Solution()
    strs1 = ["flower", "flow", "flight"]
    strs2 = ["dog", "racecar", "car"]
    result1 = solution.longestCommonPrefix(strs1)
    result2 = solution.longestCommonPrefix(strs2)
    print(f"{strs1}: {result1}")
    print(f"{strs2}: {result2}")


if __name__ == "__main__":
    main()
