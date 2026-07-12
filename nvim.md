IT

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

One important habit: don't edit the same file on both devices at the same time. Git is good at merging, but it is much easier if one device does the editing and the other receives the update. Your Python learning repo and Neovim config will stay much cleaner this way.



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




                                            MOVE FILES 

If you are already in the folder where FILE Is located, you only need to tell mv where to move it.

For example, if your destination is your pylearn folder:

mv 00_concepts.py ~/pylearn/


If you want to move it from anywhere using the full path:

Example:

mv ~/00_concepts.py ~/pylearn/


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


