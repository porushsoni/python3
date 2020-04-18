#Functions

#Built in functions

print("Print is a function used to print a message/value passed with in double braces")

#UserDefinedFunctions

print("Here comes the discussions about User Defined functions")

# def printAllNumbersInGivenRange():
#     for i in range(10):
#         print(i)
#     print("End of Function")
#
# print("Calling the function")
# printAllNumbersInGivenRange()

#Types of Arguments

#
# def addingTwoIntegers(a,b):
#     print(a+b)
# addingTwoIntegers(10,20)
#
# #Keyword Argument
#
# def addingNum(a,b):
#     print(a+b)
# addingNum(b=100,a=200)
#
#
# def printName(name):
#     NamePrint = "Hi Mr "+name+" Welcome to the world of Python"
#     print(NamePrint)
#
# printName("Porush")

#Default Variables
#
# def studentDetails(Name,Age,Category="Student"):
#     print("Name is {}".format(Name))
#     print("Age is {}".format(Age))
#     print("Category is {}".format(Category))
#
# studentDetails("Porush", 37, "Professional")
# studentDetails("Rohit", 40)
# studentDetails("Ashish", 35,"Tuter")

#Variable length argunement
print("Variable length arguments starts from here")

def printSalaries(*salary):
    print("Type of data is ", type(salary))
    for i in salary:
        print(i)
printSalaries(1)
printSalaries(1,"Porush")
printSalaries(1,"Porush","Verma")