GIT

Neovim = write/edit code
Terminal = save/version/sync code (Git)

🧠 1️⃣ Where do I  type Git commands?
Always in Termux/terminal, like this:

~/pylearn $


🟢 First time on a device:

Download the entire project from GitHub onto this computer
git clone https://github.com/r13t0/pylearn.git
✔ It copies your code to the desktop
✔ It also includes Git history
✔ It becomes a linked repo (not just files)


🔵 Every time after that:

git pull
Only when:
You already cloned the repo
AND later you made changes somewhere else (Android)
write code on android/desktop → commit → push
run: git pull → get updated code
<<<<<<< HEAD

Your local changes to the following files would be overwritten by merge.
Please commit your changes or stash them before you merge.

That message means Git is protecting your work.

It usually looks something like:

Your local changes to the following files would be overwritten by merge.
Please commit your changes or stash them before you merge.

Git is saying:

> "You have uncommitted changes on your laptop. If I pull now, those changes might be lost."



You have three choices:

1. Keep your changes (recommended if you want them)

Commit them:

git status
git add .
git commit -m "Describe your changes"
git pull

2. Keep your changes, but don't commit yet

Stash them temporarily:

git stash
git pull
git stash pop

This hides your changes, pulls the latest code, then reapplies your changes.

3. You don't need your local changes

Discard them:

git restore .
git pull

⚠️ This permanently deletes any uncommitted changes.


---

First, find out what changed

Before deciding, run:

git status

Then paste the output here. That will tell us whether you should commit, stash, or discard the changes.


ANDROID
🔴 When you change code:

git add .
git commit -m "update"
git push 



What this means: 👉 “upload to cloud”
✔ Save changes locally (commit)
✔ Upload to GitHub (push)
=======
ub (push)
>>>>>>> 89fc7527c33223b47e2a1ea10fa32941c16be5e3
✔ Now other devices can see it



-------------------------------------------------------------------

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
mv file                 :mv script.py path/to/folder/

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

---

Run this exact command in your terminal to instantly create all three files inside that specific folder:

Use curly braces {} to list your file names, and place the path to your target directory right in front of them:
    
touch path/to/your/dir/{main,utils,config}.py

touch pylearn/basics/{02_conditions,03_functions,04_loops}.py

⚠️ One Important Check

Make sure you do not put a space between the slash / and the opening brace
{.
 Correct: pylearn/basics/{02_conditions... (Creates them inside the folder)
Incorrect: pylearn/basics/ {02_conditions... (Creates them in your current folder instead)

Safety Step (If the folders do not exist yet)

The touch command will throw an error if the pylearn/basics folders do not exist yet. Run this one-liner to safely create the folders and the files all at once:

mkdir -p pylearn/basics && touch pylearn/basics/{02_conditions,03_functions,04_loops}.py

----------------


                            saving text from the terminal


Option 1: Use Neovim (Recommended)
nvim script.py


Option 2: Use the cat Command (No Editor Neede
cat > script.py << 'EOF'

2. Paste or type your long code or text. Pressing Enter will just move to the next line.

3. Type EOF on a blank line by itself and press Enter to finish and save:
EOF

Option 3: CLIPBOARD
On Android (Termux):Install the API tools first (pkg install termux-api), then run: termux-clipboard-get > script.py

On Linux Mint:Install xclip (sudo apt install xclip), then run:
xclip -selection clipboard -o > script.py 

-------------

                               DELETE FILES
Single file: Use rm filename.txt.
Multiple specific files: Use rm file1.txt file2.txt file3.txt.
All files in current folder: Use rm *.
Prompt before deletion: Use rm -i filename.txt to ask for confirmation.

Delete Directories (Folders)
Empty directory: Use rmdir folder_name.

Non-empty directory: Use rm -r folder_name to delete the directory and everything inside it recursively.

Force delete directory: Use rm -rf folder_name to bypass confirmation prompts and override read-only files.


Pro Tips for Termux
        Handle spaces: Wrap names with spaces in quotes, like rm -rf "my folder name".
        Autocompletion: Type the first few letters of a file or folder and hit the TAB key on your Termux keyboard extra bar to autocomplete the name automatically





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







#=====================================
# STRINGS 
#====================================


- Concept: String Extraction Pattern

When data is embedded inside text:

1. Find a reliable marker.
2. Slice relative to that marker.
3. Clean the extracted text if necessary.
4. Convert it to the required data type.
