print('**** Welcome to the LAB grade calculator! ****\n')
name = input('Who are we calculating grades for? ==> ')
print()
labs = float(input('Enter the Labs grade? ==> '))
if labs < 0:
    print('The lab value should have been zero or greater. It has been changed to zero.')
    labs = 0
elif labs > 100:
    print('The lab value should have been 100 or less. It has been changed to 100.')
    labs = 100
print()
exams = float(input('Enter the EXAMS grade? ==> '))
if exams < 0:
    print('The exam value should have been zero or greater. It has been changed to zero.')
    exams = 0
elif exams > 100:
    print('The exam value should have been 100 or less. It has been changed to 100.')
    exams = 100
print()
attendance = float(input('Enter the Attendance grade? ==> '))
if attendance < 0:
    print('The attendance value should have been zero or greater. It has been changed to zero.')
    attendance = 0
elif attendance > 100:
    print('The attendance value should have been 100 or less. It has been changed to 100.')
    attendance = 100
print()
weighted_grade = (labs*0.7, exams*0.2, attendance*0.1)
grade_sum = sum(weighted_grade)
print('The weighted grade for {} is {}'.format(name, grade_sum))
if grade_sum >= 90 and grade_sum <= 100:
    print('{} has a letter grade of A'.format(name))
elif grade_sum >= 80 and grade_sum <= 90:
    print('{} has a letter grade of B'.format(name))
elif grade_sum >= 70 and grade_sum <= 80:
    print('{} has a letter grade of C'.format(name))
elif grade_sum >= 60 and grade_sum <= 70:
    print('{} has a letter grade of D'.format(name))
elif grade_sum >= 0 and grade_sum <= 60:
    print('{} has a letter grade of F'.format(name))
print()
print('**** Thanks for using the Lab grade calculator ****')
input('Press ENTER to exit')
