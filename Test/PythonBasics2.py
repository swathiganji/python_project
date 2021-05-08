
#if,elif,else
num = 0
if num > 0:
    print("The num is positive number")
elif num == 0:
    print("num is zero")
else:
    print("The num is negative number")
#for loop
x =[1,2,3,4,5]
sum = 0
for val in x:
    sum = sum+val
print("Total is ", sum)

fruits =["apple","Banana", "orange"]
for val in fruits:
    print(val)
else:
    print("No fruits left")
#while loop
print("Enter a number: ")
num = int(input())
sum= 0
i=1
while i<num:
    sum = sum+i
    i=i+1
print("Total is:" , sum)