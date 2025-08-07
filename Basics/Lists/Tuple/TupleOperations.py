tuple2 = (34, 13, "fnvj", (23, 5.4))
# tuple2[2] = 45
# print(tuple2) # 'tuple' object does not support item assignment

tuple2 = tuple2 + (54,57)
# print(tuple2) # error
tuple1 = (35, 34, "243")
# print(tuple1.__len__())

#Testing Membership operators on Tuple  - not in & in
tuple1 = (35, 34, "243")
# print(10 not in tuple1)
# print(10 in tuple1)

#Concatenation of Tuple
tuple1 = (35, 34, "243")
tuple3 = (34, 78, 7)

tuple3 = tuple1 + tuple3
print(tuple3) # (35, 34, '243', 34, 78, 7)
tuple4 = tuple3 + tuple1
print(tuple4) #(35, 34, '243', 34, 78, 7, 35, 34, '243')

tuple5 = tuple1, tuple3
# print(tuple5) #((35, 34, '243'), (35, 34, '243', 34, 78, 7))

#Multiplying Tuple
tuple1 = (35, 34, "243")
tuple7 = tuple1 *3
# print(tuple7) #(35, 34, '243', 35, 34, '243', 35, 34, '243')

# Built-in Tuple functions
tuple1 = (35, 34, "243", 34)
print(tuple1.count(34))

# Deleting TUple
del tuple7
# print(tuple7)  #name 'tuple7' is not defined. Did you mean: 'tuple2'?