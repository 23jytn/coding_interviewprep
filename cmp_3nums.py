# A program to compare three numbers and print in decreasing order

print "type first number:"
num1 = int(raw_input())
print "type second number:"
num2 = int(raw_input())
print "type third number:"
num3 = int(raw_input())

if num1 > num2 and num1 > num3 :
    print num1 
    if num2 > num3 :
        print num2
        print num3
    else :
        print num3
        print num2

elif num2 > num1 and num2 > num3 :
    print num2
    if num1 > num3 :
        print num1
        print num3
    else :
        print num3
        print num1

else :
    print num3
    if num2 > num1 :
        print num2
        print num1
    else :
        print num1
        print num2
