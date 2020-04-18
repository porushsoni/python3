#Lists

# L1 = ["Porush", "Verma", 100, 10.2, True]
#
# print(type(L1))
# print(L1)

teachers = ["Ashish", 102, "Automation"]
dept1 = ["CS", 100]
print("The teachers are {}".format(teachers))
print("The name of teacher is {}, code is {}, Department is {}".format(teachers[0], teachers[1], teachers[2]))
print("The department for dept 1 is {}, code is {}".format(dept1[0], dept1[1]))

#List is mutable

L = [0,1,2,3,4]
print(L)
L[2] = "Porush"
print(L)
del L[3]
print(L)

#Operations on list
#1. Repeation list
print(L*2)
#2. Concatination list
L1 = [1,1,1]
print(L+L1)
# #3. Membership Operation
# print(6 in L)
# print (1 in L1)
# #4. Iteration
# for i in L1:
#     print(i)
# #5. Add an element
# L1 = []
# n = int(input("Enter how many elements you want in the elements of List   - "))
# for i in range(0,n):
#     L1.append(input("Enter the next element - "))
# print(L1)

#Inbuild functions of list
# L = [1,2,3,4]
# print(max(L))
# print(min(L))
# print(len(L))
# ab = "Porush"
# print(list(ab))
# ab = "Verma"
# L1 = list(ab)
# print(L1)

#Tuples
#
# T1 = ("Porush", "Verma", 101)
# print(type(T1))
# print(T1)
#
# L1 = ["Porush", "Verma", 101]
# print(type(L1))
# print(T1)

#Dictionary

dict1 = {"Name":"Porush", "Last":"Verma", "Age":37}
print(type(dict1))
print(dict1)
print("First Name of the person is {}".format(dict1["Name"]))
print("Last Name of the person is {}".format(dict1["Last"]))
print("Age of the person is {}".format(dict1["Age"]))

dict1["Name"] = "Sohan"
dict1["Last"] = "Singh"
print(dict1)

del dict1["Age"]
print(dict1)

for i in dict1.values():
    print(i)

print("the name of the person under dictionary is {}".format(dict1["Name"]))
