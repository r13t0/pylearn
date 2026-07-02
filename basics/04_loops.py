To track the largest and smallest numbers, your tracking variables must be initialized outside the loop.

If you put them inside the loop, the program will reset those tracking variables back to their starting values on every single iteration, wiping out any progress you have made.

Why Outside the Loop?

Outside the Loop: Variables act as a permanent memory. The loop updates them only when it finds a new maximum or minimum.

Inside the Loop: Variables are re-created fresh on every turn of the loop, forgetting the numbers checked previously.

Correct ImplementationHere is how to properly structure your code using a for loop:

 numbers = [4, 12, 3, 19, 7]

 # 1. INITIALIZE OUTSIDE THE LOOP
 # Set them to the first number in your collection
 largest = numbers[0]
 smallest = numbers[0]

 # 2. RUN THE LOOP
 for num in numbers:
      # Update variables inside the loop based on conditions
             if num > largest:
                         largest = num
                             if num < smallest:
                                         smallest = num

                                         # 3. USE THE RESULTS OUTSIDE THE LOOp
                                         print("Largest:", largest)
                                         print("Smallest:", smallest)

Alternative Initialization 

If you are processing dynamic user inputs via a while loop where you don't have an initial list, initialize your variables to None or mathematical infinity outside the loop:


# Initialize outside the loop
largest = float('-inf')  # Any real number will be larger than negative infinity
smallest = float('inf')  # Any real number will be smaller than positive infinity

while True:
    user_input = input("Enter a number (or 'done' to exit): ")
    if user_input == 'done':
        break
        
    num = int(user_input)
    
    # Update variables inside the loop
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

============

break = EXIT the loop completely

while True:
    if condition:
        break

Meaning:
    
“Stop the entire loop now. Never come back.”        

loop ends permanently
program moves to next section after loop

🟡 continue = SKIP this iteration only

if invalid:
    continue

Meaning:
“Ignore this input, restart loop immediately” 

What it does in real life:
this iteration is discarded
loop continues with next input

break    → kill the loop
continue → skip current turn

🎯 Visual model (very important)
Loop running:

Input 1 → process
Input 2 → process
Input 3 → invalid → continue (skip)
Input 4 → process
Input 5 → done → break (stop everything)
