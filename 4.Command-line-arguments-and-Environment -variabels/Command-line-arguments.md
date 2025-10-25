# Command Line Arguments
Python Command Line Arguments provides a convenient way to accept some information at the command line while running the program. We usually pass these values along with the name of the Python script.

To run a Python program, we execute the following command in the command prompt terminal of the operating system. For example, in windows, the following command is entered in Windows command prompt terminal.

```$ python script.py arg1 arg2 arg3```

Here Python script name is script.py and rest of the three arguments - arg1 arg2 arg3 are command line arguments for the program.

If the program needs to accept input from the user, Python's input() function is used. When the program is executed from command line, user input is accepted from the command terminal.

## Example
```
name = input("Enter your name: ")
print ("Hello {}. How are you?".format(name))
```

The program is run from the command prompt terminal as follows −


command prompt
Passing Arguments at the Time of Execution
Very often, you may need to put the data to be used by the program in the command line itself and use it inside the program. An example of giving the data in the command line could be any DOS commands in Windows or Linux.

In Windows, you use the following DOS command to rename a file hello.py to hi.py.

```C:\Python311>ren hello.py hi.py```

In Linux you may use the mv command −

```$ mv hello.py hi.py```

Here ren or mv are the commands which need the old and new file names. Since they are put in line with the command, they are called command-line arguments.

You can pass values to a Python program from command line. Python collects the arguments in a list object. Python's sys module provides access to any command-line arguments via the sys.argv variable. sys.argv is the list of command-line arguments and sys.argv[0] is the program i.e. the script name.

## Example
The hello.py script used input() function to accept user input after the script is run. Let us change it to accept input from command line.

```import sys
print ('argument list', sys.argv)
name = sys.argv[1]
print ("Hello {}. How are you?".format(name))
Run the program from command-line as shown in the following figure −
```

command-line
The output is shown below −

```
C:\Python311>python hello.py Rajan
argument list ['hello.py', 'Rajan']
Hello Rajan. How are you?
```

The command-line arguments are always stored in string variables. To use them as numerics, you can them suitably with type conversion functions.

## Example
In the following example, two numbers are entered as command-line arguments. Inside the program, we use int() function to parse them as integer variables.

```
import sys
print ('argument list', sys.argv)
first = int(sys.argv[1])
second = int(sys.argv[2])
print ("sum = {}".format(first+second))
```

It will produce the following output −

```
C:\Python311>python hello.py 10 20
argument list ['hello.py', '10', '20']
sum = 30
```
