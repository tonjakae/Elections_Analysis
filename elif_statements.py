# What is the score? Wrap input statement in int() to convert from string to integer
score = int(input("What is your test score?"))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')        
elif score >= 60:
    print('Your grade is a D.')            
else:
    print('Your grade is an F.')