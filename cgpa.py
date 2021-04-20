
print("This program calculates your GPA...have fun")
course_titles = []
credit_load = []
Grade = []
cl = []
name = input('Hi, what is your name?  ')
matriculation_number = input('what is your matriculation number?  ')
course_num = int(input('How many courses are you offering? Please state: '))
for Courses in range(course_num):
    course_title = input('Input course title: ')
    course_titles.append(course_title)
    Credit_load = int(input(f'input the credit load of {course_title}: '))
    credit_load.append(Credit_load)
    grade = (input(f'input grade for {course_title}: '))
    Grade.append(grade)
if grade == 'A' or 'a':
    cl.append(Credit_load * 5)
elif grade == 'B' or 'b':
    cl.append(Credit_load * 4)
elif grade == 'C' or 'c':
    cl.append(Credit_load * 3)
elif grade == 'D' or 'd':
    cl.append(Credit_load * 2)

ans = sum(cl) / sum(credit_load)
print("""                              



""")
print(name)
print(matriculation_number)

print('COURSE_TITLE   CREDIT_LOAD     GRADE')

for i in range(course_num):
    print(course_titles[i], credit_load[i], Grade[i])

print('Your GPA is : ', ans)








