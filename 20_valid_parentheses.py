class Solution:
    def isValid(self, s: str) -> bool:
        brackets_stack = []
        brackets_dict = {")": "(", "]": "[", "}": "{"}
        for bracket in s:
            if bracket in brackets_dict.values():
                brackets_stack.append(bracket)
            elif not brackets_stack or brackets_stack.pop() != brackets_dict[bracket]:
                return False
        
        if len(brackets_stack) != 0:
            return False
        return True

def main():
    solution = Solution()
    s1 = "()"
    s2 = "()[]{}"
    s3 = "["
    s4 = "([])"
    result1 = solution.isValid(s1)
    result2 = solution.isValid(s2)
    result3 = solution.isValid(s3)
    result4 = solution.isValid(s4)
    print(f"{s1}: {result1}")
    print(f"{s2}: {result2}")
    print(f"{s3}: {result3}")
    print(f"{s4}: {result4}")


if __name__ == "__main__":
    main()
