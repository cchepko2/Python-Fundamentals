nums = [2,4,5,6,7]

def largest(num1, num2, num3, num4, num5):
    if( num1 > num2 and num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5):
        return num1
    elif(num2 > num3 and num2 > num4 and num2 >num5):
        return num2
    elif:
    
def largest2(num1, num2, num3, num4, num5):
    maximum = num1
    if(num2 > maximum):
        maximum = num2
    if(num3 > maximum):
        maximum = num3
    if(num4 > maximum):
        maximum = num4
    if(num5 > maximum):
        maximum = num5
    return maximum

def largest(nums):
    maximum = nums[0]
    for num in nums:
        if num > maximum:
            maximum=num
    return maximum