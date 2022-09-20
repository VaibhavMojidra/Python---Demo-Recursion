#Recursion

#This function return sum of all number for given range eg 4-8 = 4+5+6+7+8 =30

def getSumOfNumbersBetween(lowerLimit,upperLimit):
    if lowerLimit>upperLimit:
        return 0
    return lowerLimit+getSumOfNumbersBetween(lowerLimit+1,upperLimit)


print("Sum of numbers between 4-8: "+str(getSumOfNumbersBetween(4,8)))
