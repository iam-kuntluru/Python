
# Loops in Python (for and while)

## Introduction

Loops are a fundamental concept in programming, and they allow you to perform repetitive tasks efficiently. In Python, there are two primary types of loops: "for" and "while."

## For Loop

The "for" loop is used to iterate over a sequence (such as a list, tuple, string, or range) and execute a set of statements for each item in the sequence. The loop continues until all items in the sequence have been processed.

**Syntax:**

```python
for variable in sequence:
    # Code to be executed for each item in the sequence
```
```
for iterating_var in sequence:
   statement(s)
```

Here, the iterating_var is a variable to which the value of each sequence item will be assigned during each iteration. Statements represents the block of code that you want to execute repeatedly.

Before the loop starts, the sequence is evaluated. If it's a list, the expression list (if any) is evaluated first. Then, the first item (at index 0) in the sequence is assigned to iterating_var variable.

During each iteration, the block of statements is executed with the current value of iterating_var. After that, the next item in the sequence is assigned to iterating_var, and the loop continues until the entire sequence is exhausted.

**Example:**

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

**Output:**

```
apple
banana
cherry
```

In this example, the loop iterates over the "fruits" list, and in each iteration, the "fruit" variable takes on the value of the current item in the list.

**Example**
The following example compares each character and displays if it is not a vowel ('a', 'e', 'i', 'o', 'u').

```
zen = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
'''
for char in zen:
   if char not in 'aeiou':
      print (char, end='')

```
On executing, this code will produce the following output −

**Output**

```
Btfl s bttr thn gly.
Explct s bttr thn mplct.
Smpl s bttr thn cmplx.
Cmplx s bttr thn cmplctd.
```

#### While Loop

The "while" loop continues to execute a block of code as long as a specified condition is true. It's often used when you don't know in advance how many times the loop should run.

A while loop in Python programming language repeatedly executes a target statement as long as the specified boolean expression is true. This loop starts with while keyword followed by a boolean expression and colon symbol (:). Then, an indented block of statements starts.

Here, statement(s) may be a single statement or a block of statements with uniform indent. The condition may be any expression, and true is any non-zero value. As soon as the expression becomes false, the program control passes to the line immediately following the loop.

If it fails to turn false, the loop continues to run, and doesn't stop unless forcefully stopped. Such a loop is called infinite loop, which is undesired in a computer program.

**Syntax:**

```python
while condition:
    # Code to be executed as long as the condition is true
```

**Example:**

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

**Output:**

```
0
1
2
3
4
```

**Example**
The following example illustrates the working of while loop. Here, the iteration run till value of count will become 5.

```
count=0
while count<5:
   count+=1
   print ("Iteration no. {}".format(count))

print ("End of while loop")
```

On executing, this code will produce the following output −
```
Iteration no. 1
Iteration no. 2
Iteration no. 3
Iteration no. 4
Iteration no. 5
End of while loop
```

In this example, the "while" loop continues to execute as long as the "count" is less than 5. The "count" variable is incremented in each iteration.
