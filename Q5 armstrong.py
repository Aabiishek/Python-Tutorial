#Armstrong of a number
n = input("Enter the number")
m = list(n)
sum = 0
l = len(n)
for i in range(m):
    temp = i ** l
    sum += temp
if n == sum:
    print("The number is Armstrong")
else:
    print("The number is not Armstrong")


    
