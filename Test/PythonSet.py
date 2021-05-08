
my_set = {"Pen", "Board", "Duster"}
print(my_set)
for val in my_set:
    print(val)
my_set.update(["marker","pencil"])
print(my_set)
my_set.add("ChromeBook")
print(my_set)
my_set.remove("Duster")
print(my_set)
my_set.discard("Pen")
print(my_set)
#my_set.remove("Duster")
my_set.discard("Pen")
my_set.pop()
print(my_set)
my_set.clear()
print(my_set)

del my_set

my_set_2={"Apples",1, 2, (3, 4, 5)}
print(my_set_2)
list = [1, 2, 3]
print(list)
my_set_3=set(list)
print(my_set_3)

#UNION | INTERSECTION | DIFF | SYMMERTIC DIFF
A = {'A','B', 1, 2, 3}
B = {'B','C',3, 4, 5}
#UNION
print(A.union(B))
print(A|B)
#INTERSECTION
print(A.intersection(B))
print(A&B)
#DIFF
print(A.difference(B))
print(A-B)
#SYMMERTIC DIFF
print(A.symmetric_difference(B))
print(A^B)
