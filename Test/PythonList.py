my_list = ["New York","Texas","Florida"]
print(my_list)
print(my_list[2])
for val in my_list:
    print(val)
print(my_list)
my_list.append("california")
my_list.pop(2)
print(my_list)
del my_list[1]
print(my_list)
print(len(my_list))
my_list.remove("New York")
print(my_list)
my_list.clear()
print(my_list)

fruits = ["Apples", "Oanges","Kiwi"]
print(fruits)
fruits.reverse()
print(fruits)

my_list_2=["apples",[1,2,3],['a','b','c']]
print(my_list_2[2][2])