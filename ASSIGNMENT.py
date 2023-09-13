'''
Assignment

A certain grade of steel is graded according to the following conditions
"	Hardness must be greater than 50
"	Carbon content must be less than 0.7
"	Tensile strength must be greater than 5600


"	     The grades are as follows:
"	Grade is 10 if all three conditions are met
"	Grade is 9 if conditions (i) and (ii) are met
"	Grade is 8 if conditions (ii) and (iii) are met
"	Grade is 7 if conditions (i) and (iii) are met
"	Grade is 6 if only one condition is met
"	Grade is 5 if none of the conditions are met
"	
Write a program, which will require the user to give values of hardness, carbon content and tensile strength 
of the steel under consideration and output the grade of the steel.
'''
h = int(input("Please enter hardness of the metal : "))
c = int(input("Please enter carbon content in the metal : "))
t = int(input("Please enter tensile strength of the metal : "))
if h > 50 and c < 0.7 and t > 5600 :
    print("Grade of the metal is 10")
elif h > 50 and c < 0.7 and t <= 5600 :
    print("Grade of the metal is 9")
elif h <= 50 and c < 0.7 and t > 5600 :
    print("Grade of the metal is 8")
elif h > 50 and c >= 0.7 and t > 5600 :
    print("Grade of the metal is 7")
elif (h > 50 and c >= 0.7 and t <= 5600) or (h <= 50 and c < 0.7 and t <= 5600) or (h <= 50 and c >= 0.7 and t > 5600) :
    print("Grade of the metal is 6")
else :
    print("Grade of the metal is 5")