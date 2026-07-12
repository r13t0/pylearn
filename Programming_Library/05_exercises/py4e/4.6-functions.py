.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function.

hours = float(input("Enter Hours:"))
rate = float(input('Enter rate per hrs:'))


#use if statement to decide overtime computation or not 
def computepay(hours, rate):
    '''
What is the job of computepay? 
Take the information needed to determine pay
and calculate the pay amount.
'''

    '''  
puts the logic to do the computation of pay in a function called computepay()
    '''
#What task is computepay supposed to perform?
# pay = computepay(hrs*rate)
    '''
How many parameters does computepay() accept? 0
How many parameters does computepay() accept?
Number of parameters
=
Number of arguments
    '''
    
    if hours > 40:  
        overtime_hours = hours - 40
        regular_pay = 40 * rate
        overtime_pay = overtime_hours * rate * 1.5
        result = regular_pay + overtime_pay
        return result
    else:
        pay = hours * rate 
        return pay 
'''
1. Computation happens in branches
2. Each branch produces a result
3. Function guarantees a return value
'''
   
    
# Repeated function calls
# computepay()
total_pay = computepay(hours, rate)
'''
Run computepay()
↓
Function returns a value
↓
Assign that value to total_pay

So the value is not trapped inside the function.
The function returns the value, and the caller can store it in a variable of its own.

'''
print("Pay", total_pay)
    
# caller    



'''
If Python receives a returned value from computepay(),
what am I doing with that returned value?
'''

'''
Autograders are not testing “truth”.
They are testing:
Plain text
Can you follow a specification exactly?
That is different from:
Plain text
Can you solve the problem?

Why schools use autograders like this
Because they force this skill:
Plain text
“Can you follow exact requirements even when your solution already works?”
That’s a real engineering skill.
Not just coding.

What this actually trains in your brain
You are building:
1. Precision thinking
No “almost correct” outputs.
2. Contract awareness
Functions are contracts:
Plain text
input → expected output format
3. Discipline over intuition
Even if your solution “feels right,” you must match spec.

what does it teach for real life practicality?
It teaches:
Plain text
Writing correct code is not enough.
You must write code that integrates correctly with other systems.
That’s literally most of software engineering.
'''
