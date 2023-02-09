# list1 = [[100, 500, 600], [900, 500, 300]]
# rows = 3
# cols = 2
# newList = []
# list2 = []
# for i in list1:
#     for j in i:
#         newList.append(j)
# c = 0
# for i in range(rows):
#     list2.append([])
# print(list2)
# for i in list2:
#     for j in newList:
        
# a = [
#     [100, 500, -600],
#     [900, -500, -300]
# ]
# for i in range(len(a)):
#     if i%2==0:
#         if sum(a[i])==0:
#             print(i)

# word = 123501
# # half1 = len(str(word))/2
# # print(half1)
# if len(str(word))%2==0:
#     print('asdasd')
#     half1 = len(str(word))/2
#     # if sum(int(str(word)[int(half1):])) == sum(int(str(word)[:int(half1)])):
#     c1 = 0
#     c2 = 0

#     for j in (str(word)[:int(half1)]):
#         c2 += int(j)
#     for i in (str(word)[int(half1):]):
#         c1 += int(i)
#     if c1 == c2:
#         print(True)
#         print(c1, c2)
#     else:
#         print(False)
#         print(c1, c2)
# else:
#     half1 = len(str(word))//2
#     # if sum(int(str(word)[int(half1):])) == sum(int(str(word)[:int(half1)])):
#     c1 = 0
#     c2 = 0
#     for i in (str(word)[int(half1)+1:len(str(word))+2]):
#         c1 += int(i)
#     for j in (str(word)[:int(half1)]):
#         c2 += int(j)
#     print(c1, c2)
#     if c1 == c2:
#         print(True)
#         print(c1, c2)
#     else:
#         print(False)
#         print(c1, c2)

# s = input()
# c1 = s[:(len(s) + 1) // 2]
# c2 = s[(len(s) + 1) // 2:]
# print(c1, c2)

# source = "ollheaaaewrdbfsg"
# destination = "hello"

# source = source.split()
# destination = destination.split()
# print(source)
# print(destination)
# matrix = [
#     [100, 500, -600],
#     [900, -500, 300],
#     [300, 89, -200]
# ]


# def find(matrix):
#     for row in range(len(matrix)):
#         if row%2==0:
#             c=0
#             for i in matrix[row]:
#                 c += i
#             if c==0:
#                 print(row)
# find(matrix)

# Input = input()
# h1 = 0
# h2 = 0
# if len(str(Input)) % 2 == 0:
#     halves = len(str(Input)) / 2
#     for j in (str(Input)[:int(halves)]):
#         h2 += int(j)
#     for i in (str(Input)[int(halves):]):
#         h1 += int(i)
#     if h1 == h2:
#         print(True)
#         print(h1, h2, ' - happy')
#     else:
#         print(False)
#         print(h1, h2, ' - unhappy')
# else: print('не получилось(')

# a = [1, 2, 1, 2, 2, 1, 3, 4]
# b = [7, 2, 1, 1, 5, 6]
# for i,j in zip(a,b):
#     print(i, j)

# a = [
#     [100, 500, -1000],
#     [900, -500, 300],
#     [300, 89, -200]
# ]


# for i in a:
#     c = 0
#     for j in range(len(i)):
#         if j%2==0:
#             c += i[j]
#     if c<0:
#         print(a.index(i))

# def find(matrix):
#     for row in matrix:
#         count = 0
#         for element in range(len(row)):
#             if element%2==0:
#                 count += row[element]
#             if c<0:
#                 print(row)

# matrix = [
#     [100, 500, -600],
#     [900, -500, 300],
#     [300, 89, -200]
# ]
# find(matrix)

# list1 = ['Alexey', 'Islam', 'Nurym']
# '''      0  1  2  3  4  5  6'''

# # for i in range(len(list1)):
# #     print(list1[i])
# # list1[-1]
# list1[0] = 'Kanysh'
# del list1[0]
# list1.insert(0, 'Madi')
# list1.append('Alexey')
# print(list1)
# firstName = 'Kanysh'
# surname = 'Beisenbek'
# print(firstName[0], surname[0])

# distance = 5.17, 5.20, 10.5, 15

# distance[0] = 4.0

# dict = {
#     key: value
# }

# raceTimes = {
#     'Екатерина': 26,
#     'Madi': 20,
#     'Kanysh': 22
# }

# raceTimes['Екатерина'] = 19
# print(raceTimes)

# del raceTimes['Kanysh']
# print(raceTimes)
# print(raceTimes['Екатерина'])
# for i in raceTimes:
#     print(i, raceTimes[i])


# list1 = [
#     [0, 1, 2, 3],
#     [2, 0, 4, 5]
# ]
# for i in list1:
#     for element in i:
#         print(element)

# distance = 2.0, 4.15, 45.2

# for i in distance:
#     print(i)


# listThreeDimension = [
#     [[0, 1, 2, 3], [0, 1, 2, 3, 4, 5]],
#     [[2, 4, 5, 6], [7, 8, 15, 68]]
# ]

# for i in listThreeDimension:
#     for j in i:
#         print(j)

''''''

# class Student:
#     def __init__(self, age, name):
#         self.name = name
#         self.age = age
#         self.grades = []
print(1)

