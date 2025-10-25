# Environment Variables

Environment variables are key-value pairs stored in the OS environment.
You can use them to store sensitive info like passwords, tokens, or configuration paths.

Setting an Environment Variable:
Windows (CMD)
```
set MY_VAR=HelloWorld
```

Linux/Mac
```
export MY_VAR=HelloWorld
```

Accessing in Python:

```
import os

value = os.getenv("MY_VAR")
print("Value of MY_VAR:", value)
```

Setting inside Python:

```
import os

os.environ["MY_VAR"] = "DevOps"
print(os.getenv("MY_VAR"))
```


## Example:

```
import sys 

def addition (num1, num2, num3):
    add = num1 + num2 + num3
    return add

def sub(num1, num2):
    s = num1 - num2
    return s 

def mul(num1, num2):
    m = num1 * num2
    return m 

num1 = float(sys.argv[1])
operation = sys.argv[2]

if operation == "add":
    num2 = float(sys.argv[3])
    num3 = float(sys.argv[4])
    output = addition(num1, num2, num3)
    print(output)

elif operation == "sub":
    num2 = float(sys.argv[3])
    output = sub(num1, num2)
    print(output)

elif operation == "mul":
    num2 = float(sys.argv[3])
    output = mul(num1, num2)
    print(output)

  ```
