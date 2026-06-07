
Create folder           :mkdir folder_name
open file inside folder :nvim folder name/file name.py
open file               :nvim file.py
go into folder          :cd folder_name
create file             :nvim new.py
create from inside Nvim 
create inside specific directory :e path/to/folder/filename.py/txt
open file inside nvim   :e file.py
save file               :w quit                    
:q save + quit             :wq
quit without saving     :q!
delete file (terminal)  :rm file.py
delete current file     :!rm %
Search concept          :/
nxt result              :n
previous result         :N
view files              :ls

access init.lua - Terminal  ls -a ~/.config/nvim/


execute file            :!python3 %
terminal                :term python3 %
key shortcut            : :spacebar + r 
from terminal           : python file.py

NAVIGATE THE TREE

1. run: Ex 
2. mv cursor to a file
3. press enter
4. open file

OPEN TREE ON LEFT SIDE

:Vex

Now:
left side → folder tree
right side → file


CLOSE TREE

:q


SWITCH TO FILE

:b 1

OR 

:b file.py

NXT FILE
:bn

PREVIOUS FILE
:bp


"""
PYTHON CONCEPTS REFERENCE
Use this file for QUICK REVIEW and SEARCHING.
Each section = one core idea.
Keep examples SMALL and CLEAR.
"""

# ====================
# VARIABLES
# ====================

score =  0
name = 'risto'


# ==========
# OUTPUT
# ==================

''' Print statement with Quotes create text
print("10=10) = 10*10

while no quotes refer to calculatinng
print(10*10) = 100
'''

print() just talks: It shows text to the human watching the screen. The computer cannot use that text for math or logic later. It is a "dead end."

# ====================
# INPUT / OUTPUT
# ====================



# ====================
# TYPE CONVERSION
# ====================

Reusing the same name to convert
rate_per_hr = float(rate_per_hr)

How to Convert in the Input Line
hrs = float(input("Enter Hours: "))


# ====================
# IF STATEMENT
# ====================

Order Matters 
Check valid scores from highest to lowest





 # ====================
 # IF / ELSE
 # ====================



# ====================
# ELIF
 # ====================


==============================
Boolean Operators
==============================


global is about:
Plain text
Where a variable lives.
Example mentally:
Plain text
Function and outside code
sharing the same variable.






# ====================
# FUNCTIONS
# ====================



++++++++++++++++++++++++++
Global keyword
++++++++++++++++++++++++++






# ====================
# FUNCTION WITH PARAMETERS
# ==================== 





When a function "returns a value," it means the function calculates a   
result and sends that result back to the line of code that called it.


=++++++++++++++++++=====

# recognize when a problem wants parameters vs input 
# inside the function
==============================



# ====================
# RETURN VALUES
# ====================

Give a value back to whoever called me.

Sending a value back to the caller.
Function computes result
↓
hands result back
↓
caller stores it

1. Hand back the value
2. Exit the function immediately
Any code inside that function below the return will not execute.


return actually gives data: It gives the data back to the computer program.You can save it, change it, or pass it into another function.

use the return keyword to pass the value back

def add_numbers(a, b):
        result = a + b
            return result  # This sends the answer back out of the functio

        # Catch the returned value in a variable        
        total = add_numbers(5, 10) 

        print(total)  # Output: 15

# ====================
# LOOPS - WHILE
# ====================




For i in range(4):
    print(i)

                                                                     
 # ====================
 # LOOPS - FOR 
 # ======================

