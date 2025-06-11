class Solution:
    def myAtoi(self, s: str) -> int:
        int_s = 0
        s = s.strip()
        is_negative = False
        int_started = False
        digits = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9":9}
        for char in s:
            if char in digits:
                int_s = int_s * 10 + digits[char]
            elif char == "-" and not int_started:
                is_negative = True
            elif char == "+" and not int_started:
                is_negative = False
            else:
                break
            int_started = True
        
        if is_negative:
            int_s *= -1
        if int_s < -2**31:
            int_s = -2**31
        elif int_s > 2**31 - 1:
            int_s = 2**31 - 1
        return int_s
        
def main():
    solution = Solution()
    s1 = "-91283472332"
    s2 = "    +-042"
    s3 = "1337c0d3"
    s4 = "0-1"
    s5 = "words and 987"
    result1 = solution.myAtoi(s1)
    result2 = solution.myAtoi(s2)
    result3 = solution.myAtoi(s3)
    result4 = solution.myAtoi(s4)
    result5 = solution.myAtoi(s5)
    print(f"{s1}: {result1}")
    print(f"{s2}: {result2}")
    print(f"{s3}: {result3}")
    print(f"{s4}: {result4}")
    print(f"{s5}: {result5}")


if __name__ == "__main__":
    main()
