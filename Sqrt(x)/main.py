class Solution:
    def mySqrt(self, x: int) -> int:
        pointerLeft, pointerRight = 0, x
        res = 0

        while pointerLeft <= pointerRight:
            m = int((pointerLeft + pointerRight) / 2)

            if (m**2 > x):
                pointerRight = m - 1
            elif (m**2 < x):
                pointerLeft = m + 1
                res = m
            else:
                return m
        return res

print(Solution().mySqrt(4))


# FirstSolution

# def mySqrt(self, x: int) -> int:
#     x = x**(1/2)
#     return int(x)