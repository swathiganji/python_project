
my_tuple = ("Apple","Banana","cherry")
print(my_tuple)
print(my_tuple[2])
print(len(my_tuple))
for val in my_tuple:
    print(val)

my_tuple_2 =("Apple",(1,2,3),['a','b','c'])
my_tuple_2[2][2]= 'd'
print(my_tuple_2)
print("Apple" in my_tuple_2)
print("Cherry" in my_tuple_2)