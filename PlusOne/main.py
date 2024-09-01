class Solution:
    def plusOne(self, digits: list):
        sum = ''
        for value in digits:
            sum += str(value)

        sum = int(sum)+1
        digitsPlusOne = []
        for digit in str(sum):
            digitsPlusOne.append(int(digit))

        return digitsPlusOne
    

print(Solution().plusOne([9]))