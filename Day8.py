#For Loop

# value_1 = input("Enter the value")
# i = 0
# for x in value_1:
#     print("The character present at {} and {}".format(i,x))
#     i = i+1
#
# for x in range(10):
#     print(x)

# for x in range(3,10):
#     print(x,end = " ")
#     print()
#
# print("Next range example")
#
# for x in range(3,10,2):
#     print(x)
#
# print("Next range example")
#
# for x in range(15,2,-2):
#     print(x)

for x in range(10):
    if x == 6:
        print(x)
        break
    else:
        continue
    print(x)
print("The execution is completed")
