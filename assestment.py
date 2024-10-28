# Financial Aid Determination

#floated values to use in if statements
income = float(input("Enter your income:"))

dependents = float(input("Enter number of dependents:"))

#Nested if statement
if income < 50000:
        if dependents >= 3:
            print("Eligible for full financial aid.")
        elif 1 <= dependents <= 2:
            print("Eligible for partial financial aid.")
elif 50000 <= income <= 75000:
        if dependents >= 3:
            print("Eligible for partial financial aid.") #using if and else statements to determine the number of dependentens and the income, depeterming the print and finiacial aid
        else:
            print("Not eligible for financial aid.")
else:  #if inc > $75,000
        print("Not eligible for financial aid.")



        
#Scholarship Eligbity 


gpa = float(input("Enter your GPA: ")) #transforms the string numbers into float, because you ask for a number

hours = float(input("Enter your service hours: "))

if gpa > 3.5: #If the gpa is higher as well as the hours being higher than 50, 
    if hours >50:
        print("Eligible for full scholarship.") #return this as a result of the other two being true
    elif hours >= 30:  #If one is false, print this, partial scholarship
        print("Eligible for partial scholarship.")
    else: #if hours are below 30,  are false, print not eligble
        print("Not eligible for scholarship.")
elif gpa < 3.0: #If gpa is lower than 3, also print not eligble
    print("Not eligible for scholarship.")
else:
    print("Not eligible for scholarship.")