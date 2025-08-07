tuple1 = (10, 20, "Sidd", 43.32, [3,"s", 5.3])
tuple2 = (34, 13, "fnvj", (23, 5.4))
tuple3 = tuple1 + tuple2
# print(tuple3)

tuple4 = (4,)
# print(tuple4)
# print(type(tuple4))
tuple5 = (4)
# tuple5 = ()
# print("type5", type(tuple5))

# Accessing tuple elements using index
i = 0
while i < tuple1.__len__():
    # print("ele at index", i, "is", tuple1[i])
    i +=1

# Negative Tuple indexing
tuple6 = (10, 20, "Sidd", 43.32, [3,"s", 5.3])
print(tuple6[-1])
print(tuple6[-3])
# print(tuple6[-6]) #IndexError: tuple index out of range

# Using for loop-
print("Using for loop-")
for ele in tuple6:
    print(ele)

# Slicing in Tuple
tuple7 = ('p', 'y', 't', 'h', 'o', 'n')
print(tuple7[2:])
print(tuple7[:5])
print(tuple7[2:-2])

