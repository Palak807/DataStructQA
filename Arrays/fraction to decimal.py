class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return "0"

        result = []
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")

        numerator = abs(numerator)
        denominator = abs(denominator)

        quotient = numerator // denominator
        result.append(str(quotient))

        remainder = numerator % denominator
        if remainder == 0:
            return "".join(result)

        result.append(".")

        remainder_map = {}
        while remainder != 0:
            if remainder in remainder_map:
                result.insert(remainder_map[remainder], "(")
                result.append(")")
                break

            remainder_map[remainder] = len(result)
            remainder *= 10
            quotient = remainder // denominator
            result.append(str(quotient))
            remainder = remainder % denominator

        return "".join(result)

obj = Solution()
print(obj.fractionToDecimal(16, 13))
