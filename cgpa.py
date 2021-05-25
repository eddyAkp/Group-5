//EDNA EMMANUEL AKPAN...ENG1603855
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
    Credit_load = int(input(f'input the credit load 
