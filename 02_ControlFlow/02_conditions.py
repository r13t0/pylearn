CONDITIONAL STATEMENTS 

  STEP BY STEP METHOD TO BUILD A CONDITION


🚦 CONTROL FLOW (CONDITIONALS ONLY)

Control flow = how the program chooses what runs next.
Decision → chooses a path (if / elif / else)

A condition is a True/False test that decides what code runs.


“What do I do when I see a new problem?”


A condition is:
value + rule + comparison → True / False


Steps:

Value → what data & What does this value represent in reality?
         age → time alive

Rule → what must be true in reality? Identify COnstraint.
         age cant be negative
          passing score usually 50+,
          email - must have @

Comparison→ how do they relate? 

Example:
age >= 18

After True/False,

NEXT: 
    assign meaning to that True/False result?

Meaning = what True/False represents in the program’s context

The meaning comes from:
what the program is trying to accomplish

Then choose ONE of 3 patterns:

🔷 VALIDATION (Is it allowed?)
Used when checking rules.
age >= 18
True → allowed
False → blocked

🟡 CLASSIFICATION (What type is it?)

Used when labeling.
temp < 0
True → category A   (freezing category)
False → category B  (non-freezing category)

🔴 SELECTION (What should happen?)

Used when choosing action.
password_correct
True → do action A   (login user)
False → do action B  (deny access)

------------------------------------


⚡ ONE-LINE MEMORY

> Condition = question
True/False = answer
if/elif/else = path chooser

D = what exists (Distinguish values)
R = how it connects (Find relationship)
S = what it does (Define system behavior)
P = what it means (Assign meaning)
