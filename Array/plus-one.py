# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
def plusOne(digits):
    carrier = 1
    for i in range(len(digits)-1, -1, -1):
        temp_sum = (digits[i] + carrier)
        digits[i] = temp_sum % 10
        carrier = temp_sum // 10 
        if not carrier:
            return digits
