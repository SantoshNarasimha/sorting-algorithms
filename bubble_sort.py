list1 = [200, 0, 99, 10, 92, 88]

for i in range(len(list1)-1):

    for j in range(len(list1)-1):

        if list1[j] > list1[j+1]:

            list1[j], list1[j+1] = list1[j+1], list1[j]

print(list1)