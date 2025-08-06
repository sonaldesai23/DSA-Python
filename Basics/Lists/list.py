list1 = [10, 20, "Sidd", 43.32, [3,"s", 5.3]]
# print(list1[1])
# print(list1[-1])
# print(list1[-3])
# print(list1[-5])


list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for ele in list2:
    sq = ele*ele
    cu = ele*ele*ele
    # print("Square is:", sq)
    # print("Cube is:", cu)

list3 = ['p', 'y', 't', 'h', 'o', 'n', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
# print(list3[8:14])
# print(list3[3:8])
# print(list3[5:])
# print(list3[:7])
# print(list3[:5:2])

list4 = [10, 20, 40, 34.34, "ravi", 100]
# print("Presence of 10 in list4 ",10 in list4 )
# print("Presence of 'ravi' in list4 ","ravi" not in list4 )

list2.append(80)
# print(list2)

list1.insert(3, 100)
# print(list1)

list2.extend(list4)
print(list2)

