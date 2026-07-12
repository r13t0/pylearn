Good question. They are closely related, but they answer **different questions**.

Think of them as two levels.

---

# Pattern Composition

**Question it answers:**

> "How are the individual thinking patterns combined inside this solution?"

It is about the **relationship between patterns**.

It shows:

* which patterns exist
* which patterns are inside other patterns
* which pattern controls the flow

Example from the number exercise:

Patterns:

```
Sentinel Loop
    |
    ├── Validation
    |
    ├── Exception Handling
    |
    ├── Maximum
    |
    └── Minimum
```

Meaning:

The **Sentinel Loop** is the container.

Inside each loop cycle:

1. Get input
2. Validate it
3. Update maximum
4. Update minimum

So composition is about the **architecture of the thinking**.

---

# Pattern Pipeline

**Question it answers:**

> "What is the sequence of operations data moves through?"

It focuses on the **flow of data**.

Example:

```
Input
 ↓
Validation
 ↓
Conversion
 ↓
Maximum Comparison
 ↓
Minimum Comparison
 ↓
Output
```

The data travels through stages.

Like a factory:

```
Raw material
     ↓
Cleaning
     ↓
Processing
     ↓
Packaging
     ↓
Finished product
```

---

# The Difference

A simple comparison:

|          | Pattern Composition         | Pattern Pipeline                   |
| -------- | --------------------------- | ---------------------------------- |
| Focus    | Structure                   | Flow                               |
| Question | How are patterns organized? | What happens to data step-by-step? |
| Like     | A building blueprint        | A production line                  |
| Shows    | Relationships               | Sequence                           |
| Emphasis | Control                     | Movement                           |

---

## Same program, two views

Imagine:

```python
while True:
    value = input()

    if value == "done":
        break

    try:
        value = int(value)
    except:
        continue

    if value > largest:
        largest = value
```

---

## Composition View

"How is this solution built?"

```
Sentinel Loop
        |
        |
        +-- Validation
        |
        +-- Exception Handling
        |
        +-- Maximum Tracking
```

The loop controls everything.

---

## Pipeline View

"What path does information travel?"

```
User Input

↓

Sentinel Check

↓

Convert String → Integer

↓

Validate

↓

Compare

↓

Update Maximum

↓

Repeat
```

---

# A useful mental model

Think of a car.

## Composition:

What parts make the car?

```
Car
 |
 ├── Engine
 ├── Transmission
 ├── Brakes
 └── Steering
```

That is structure.

---

## Pipeline:

What happens when driving?

```
Fuel
 ↓
Engine
 ↓
Power
 ↓
Transmission
 ↓
Wheels
 ↓
Movement
```

That is flow.

---

For programming:

```
Pattern Composition = "What patterns make this algorithm?"

Pattern Pipeline = "How does information move through the algorithm?"
```

As you build your Programming Thinking Library, keep both:

* **Patterns** = individual tools
* **Composition** = how tools are assembled
* **Pipelines** = reusable flows of tools working together

A beginner recognizes syntax.

A programmer recognizes **compositions and pipelines**.

