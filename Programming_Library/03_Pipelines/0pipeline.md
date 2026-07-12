A **pipeline** is a sequence of steps where the **output of one step becomes the input for the next step**.

Think of it like a factory assembly line:

```
Raw material
     ↓
Cut
     ↓
Shape
     ↓
Paint
     ↓
Finished product
```

Each stage does one job, and together they create the final result.

In programming:

```
Input
  ↓
Process
  ↓
Output
```

is the simplest pipeline.

---

## Example 1: Your first program

Your name greeting program:

```python
name = input("Enter your name: ")

print("Hello", name)
```

Pipeline:

```
Input
  ↓
Assignment
  ↓
Output
```

Meaning:

1. Get data from the user.
2. Store the data.
3. Use the data.

---

## Example 2: Your pay calculator

Your second program:

```python
hours = input("Enter Hours:")
rate = input("Enter Rate:")

hours = float(hours)
rate = float(rate)

pay = hours * rate

print("Pay:", pay)
```

Pipeline:

```
Input
   ↓
Transform
   ↓
Calculate
   ↓
Output
```

Breaking it down:

### Stage 1 — Input

Get raw data.

```
"35"
"2.75"
```

At this point they are strings.

---

### Stage 2 — Transform

Convert the data.

```
"35" → 35.0
"2.75" → 2.75
```

Now Python can calculate.

---

### Stage 3 — Process

Perform the operation.

```
35.0 × 2.75 = 96.25
```

---

### Stage 4 — Output

Display the result.

```
Pay: 96.25
```

---

## Pattern vs Pipeline

This distinction is important.

### Pattern

A **single reusable thinking tool**.

Example:

```
Transform

Purpose:
Change data from one form to another.
```

Used when you think:

> "I need to convert this."

---

### Pipeline

A **combination of patterns working together**.

Example:

```
Input
 ↓
Transform
 ↓
Calculation
 ↓
Output
```

Used when you think:

> "What sequence of steps solves this whole type of problem?"

---

A good analogy:

**Patterns are Lego pieces.**

```
Counter
Filter
Transform
Validation
```

are individual blocks.

**Pipelines are the structures you build with them.**

Example:

```
Input Validation Pipeline

Input
 ↓
Validation
 ↓
Repeat if wrong
 ↓
Process
```

is made from smaller patterns:

```
Input
+ Validation
+ Sentinel Loop
+ Sequence
```

---

So in your Programming Thinking Library:

```
Algorithm Patterns
= Individual problem-solving tools

Pattern Pipelines
= Common combinations of those tools
```

As you progress, you will probably remember pipelines more than individual exercises because real programs are rarely just one pattern—they are usually **chains of patterns working together**.

