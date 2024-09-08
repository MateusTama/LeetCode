class Solution:
    def addBinary(self, a: str, b: str) -> str:
        MoreNumber = a
        LessNumber = b
        if (len(b) > len(a)):
            MoreNumber = b
            LessNumber = a
        MoreEndPointer = len(MoreNumber)
        LessEndPointer = len(LessNumber)
        CarryIn = 0 

        SumBinary = ""

        while (MoreEndPointer >= 1):
            MoreEndPointer = MoreEndPointer-1
            LessEndPointer = LessEndPointer-1

            MoreLastNumber = int(MoreNumber[MoreEndPointer])
            if (LessEndPointer >= 0):
                LessLastNumber = int(LessNumber[LessEndPointer])
            else:
                LessLastNumber = 0

            LastNumber = MoreLastNumber + LessLastNumber + CarryIn

            CarryIn = 0
            
            if (LastNumber == 2):
                LastNumber = 0
                CarryIn = 1

            if (LastNumber == 3):
                LastNumber = 1
                CarryIn = 1
            
            SumBinary += str(LastNumber)

        if (CarryIn == 1):
            SumBinary += str(CarryIn)

        return SumBinary[::-1]

            


print(Solution().addBinary("111", "1010"))