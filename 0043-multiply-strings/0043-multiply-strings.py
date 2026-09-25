class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # If either number is 0, the product is always 0
        if num1 == "0" or num2 == "0":
            return "0"

        n, m = len(num1), len(num2)
        # The maximum digits of the product of two numbers 
        # of lengths n and m is at most n + m.
        result = [0] * (n + m)

        # Multiply each digit from right to left
        for i in range(n - 1, -1, -1):
            d1 = int(num1[i])
            for j in range(m - 1, -1, -1):
                d2 = int(num2[j])
                
                mul = d1 * d2
                p1, p2 = i + j, i + j + 1  # positions in result array
                
                # Add multiplication result to the existing value at p2
                total = mul + result[p2]
                
                # Store the single digit remainder
                result[p2] = total % 10
                
                # Add the carry to the tens place position (p1)
                result[p1] += total // 10

        # Convert array to string and strip any leading zeros
        result_str = "".join(map(str, result))
        return result_str.lstrip("0")