def student(n):
    for i in range(n):
        print("Enter details for student {}:".format(i+1))
        s[i].roll = int(input("Roll Number: "))
        s[i].nam = input("Name: ")
        s[i].marks = float(input("Marks: "))

    # Sorting the students based on marks
    for i in range(n-1):
        for j in range(i+1, n):
            if s[i].marks < s[j].marks:
                s[i], s[j] = s[j], s[i]
                
    # Displaying the sorted student details
    print("\nStudent details (sorted by marks):")
    for i in range(n):
        print("Roll Number: {}".format(s[i].roll))
        print("Name: {}".format(s[i].nam))
        print("Marks: {:.2f}".format(s[i].marks))