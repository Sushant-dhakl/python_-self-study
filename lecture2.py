# num = input("enter any number")
# num = int(num)


# # for factoral

#  #fact = 1
# #while i<=num:
#   # fact = fact * i
# # i = i+1
# #print(fact)

# if (num%2==0):
#     print("Even")
# else:
#     print("Odd")

# i = 0
# while num != 0:
#     n = num % 10
#     i = i * 10 + n
#     num = num // 10 

# print(i)


class student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks  

n = int(input("enter number of student "))
students=[]

for i in range(n):
    name = input("enter  the name ")
    age = int(input("enter the age "))
    marks = float(input("enter the marks "))
    s1 = student(name,age,marks)
students.append(s1)

for s in students:
    print("Name:", s.name)
    print("Age:", s.age)
    print("Marks:", s.marks)