empId = int(input("Enter your id no. : "))
empName = input("Please enter employee name: ")
empAge = int(input("Enter age : "))
empSalary = float(input("Enter salary : "))
empDesignation = input("Enter Deignation : ")
empContactNo = int(input("Entetr Number : "))

print("\n\nYour employee id : ",empId,"   ",type(empId))
print("Your name : ",empName ,"   ",type(empName))
print("Your age : ",empAge ,"   ",type(empAge))
print("Your Salary : ",empSalary+empAge ,"   ",type(empSalary))
print("Your Designation : ",empDesignation*12 ,"   ",type(empDesignation))
print("Your Contact No. : ",empContactNo ,"   ",type(empContactNo))

a = 200
b = 99

print()
print()
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)