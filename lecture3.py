# # # # while loop 


# # # #  qn 1 prin num from 1 to  100
# # # # i=1
# # # # while i<=100:
# # # #     print(i)
# # # #     i += 1


# # # # 2 print num 100 to 1 

# # # # i=100
# # # # while i>=1:
# # # #     print(i)
# # # #     i -= 1


# # # # 3 multiplication of n 

# # # # num = int(input("enter any number"))
# # # # i=1
# # # # while i<=10:
# # # #     print(num,"*",i,"=",num*i)
# # # #     i += 1

# # # # print elements of list using loop

# # # list = [1,4,9,16,25,36]
# # # i=0
# # # while i<len(list):  # listing start from zero,  len(list) means length of list which is 6 in this case beacuse there are  6 charcters in list .
# # #     print(list[i])
# # #     i=i+1

# # # break : used to terminate the loop

# # # for eg:
# # i=1
# # while i<=10:
# #     if (i==5):  # ans will be 1 2 3 4 
# #         break
# #     print(i)
# #     i += 1


# # for loop                              it is used for sequential traversal in list, string, tuple, dictionary
# # syntax  for variable in iterable:      iterable means list, string, tuple, dictionary, range
# #           body of loop


i = {1,2,3,4,5}
for j in i:
    print(j)

# for loop with else
str = "sushant"
for j in str:
    print(j)
else:
    print("Loop completed")