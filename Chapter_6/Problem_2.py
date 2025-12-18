# Check weather the student has passed or not using if else 

marks1 = int(input("Enter your marks1 : "))
marks2 = int(input("Enter your marks2 : "))
marks3 = int(input("Enter your marks3 : "))

total_percentage = (marks1 + marks2 + marks3)/3

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("Congratulations! you have passed the exam : ",total_percentage)
    
else:
    print("You Failed! : ", total_percentage)