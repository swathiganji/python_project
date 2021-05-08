
my_dict = {"Apple":"red",
           "grapes": 20,
           "Bananas": "Yellow"}
print(my_dict)
print(my_dict["Apple"])
print(my_dict.get("Bananas"))
for x in my_dict:
    print(x)
for x in my_dict:
    print(my_dict[x])
for x,y in my_dict.items():
    print(x,y)

my_dict["grapes"]= 10
my_dict["kiwi"]= "Green"
print(my_dict)
my_dict.pop("Apple")
print(my_dict)
my_dict.popitem()
print(my_dict)
del my_dict["grapes"]
print(my_dict)
my_dict.clear()
print(my_dict)