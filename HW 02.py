# -*- coding: cp1254 -*-

#HW 2.1


#HW 2.2

S_Start = 0.2
S_End = 9.8
S_Increase = 0.2
Total = 0
Serie_Size = int(((S_End - S_Start) / S_Increase) + 1)
Count = 0
while Count < Serie_Size:
    Total += S_Start
    S_Start += S_Increase
    Count += 1
print "The Serie Total is : " + str(float(Total))

#HW 2.3

S_Start = 0
S_End = 248
S_Increase = 1
Total = 0
Serie_Size = int(((S_End - S_Start) / S_Increase) + 1)
Count = 0
while Count < Serie_Size:
    Total += S_Start**2
    S_Start += S_Increase
    Count += 1
print "The Serie Total is : " + str(Total)

#HW 2.4

S_Start = 0
S_End = 248
S_Increase = 1
Total_Amount = 0
Total_Value = 0
Serie_Size = int(((S_End - S_Start) / S_Increase) + 1)
Count = 0
Divided = 6
while Count < Serie_Size:
    A1 = Count + 1 / Divided
    if A1 % Divided == 0:
        print A1
        Total_Amount += 1
        Total_Value += A1
    Count += 1
print "The Total Value of the numbers which are divided to 6; is : " + str(Total_Value)
print "The amount of numbers which are divided to 6; is : " + str(Total_Amount)

