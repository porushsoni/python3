a = "Welcome_to_Way2_Automation"

print (a[1:8:1])
print (a[8:1:-2])
print (a[8:1:1])
print (a[-4:8:-1])


# Concatination and Repeat

a = "Porush"
b = "Verma"
print("priyanka"+"verma")
a = 10
c= 10.5
print("Porush"+str(a))

print(b+str(a))

#Interpolation Operator

a = 100
example = "This is %d %d %d %f" %(a,a,a,c)
print (example)
b = 200
example = "THis is {}".format(b)
print (example)


a = 10
b = 20
c = 30

ex = "W2A {}, {}, {}".format(a,b,c)
print (ex)

#----------
a = 10
b = 20
c = 30
temp1 = "This number is {}".format(a)
print(temp1)
temp2 = "These numbers are {} {} {}".format(10,20,30)
print(temp2)