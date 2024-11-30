# PYTHON

(SET) Become familiar with IDE
What is source code? Source code is the actual programming statements that  are created by a programmer with a text editor or an IDE, and then saved in a file. Generally, the source code file in Python ends with .py. This file contains the coding statements. You cannot use Microsoft WORD or any word processor to create the source file. You must use a text editor such as Notepad on the PC or Textedit on the Mac. A text editor does not add any special characters to the file. However, larger applications generally contain more than one source file. An IDE can help manage ALL your files.  Note: Notepad and Textedit are NOT IDEs, they are text editors.

What is an IDE?  It is an Integrated Development Environment. It is a software application that combines various tools that a developer (programmer) might need. Many IDEs contain a text editor, debugger, compiler, etc...
For example, the text editor in an IDE is specifically written to catch your programming typos, some of them at least, similar to how Word will catch some of your spelling errors. Many have debuggers to help you find your errors quickly, and to test your code. Without an IDE, a programmer would have to buy/download all these tools separately. 

Some IDEs are free, available via open source, while others are not, they are commercially sold. 

Commonly used IDEs: Microsoft Visual Studio is a common IDE used for C++, C# (C sharp), Python, Visual Basic, etc...NetBeans is a free IDE used for Java. Eclipse is also a commonly used IDE for Java. Xcode is an IDE used on Macs for Swift, C++, etc... Python comes with an IDE built in, called Python Integrated Development and Learning Environment (Python IDLE).

Requirement for this course: You are REQUIRED to download Python IDLE onto your PC (or Mac).

What should I do now? Based on whether you are a using Windows or MacOS, follow the instructions in either the How to Download Install and Use Python IDLE (Windows) or How to Download Install and Use Python IDLE (Mac).
                                   
             



# Functions:
# To group functions, we start by defining the functions #with a def keyword e.g

def greet_user():

# with the above I have define a function "greet_users():"
# then, the colon ":" marks the beginning of the code     #block that belongs to the function.

# to group codes into the funcion we indent by 2 spaces. #e.g

def greet_user():
  print("Good morning James")
  print("Welcome back")

# to run the code we call the functions, and this is done #by coding the name followed by parenthesis. 

greet_user()

# we name functions using snake case
#sometimes functions need specific information to help #them perform their tasks. 
# like using variables inside functions

def geet_ron():
  name = "Ron"
  print(f"Hello, {name}");

greet_ron()  

# len() is used in python to count number of character in #a string, but it also has other general purposes too.

course = 'Python for Beginners'
print(course.upper())
print(len(course))
print(course)
print(course.lower())


#upper() and lower() are string method functions that are #used to change characters to lower and uper cases in a #string using dot "." operator

#find() this is also another method that is used to find #the index of a character 

#e.g
course = 'Python for Beginners'
print(course.find("P"))
print(course.find("Biginners"))
print(course.find("O"))

# if you pass a character that is not in the string, it #gives you a "-1" because it cant find the character #within tyhe string

# replace() is used to replaces strings or characters

print(course.replace(Python, Java))

# in operator is used to produce a boolean value within a #string 

#E.g
 #"Python" in course
 print("Python" in course)  
 #will return True, because we have Python in Course, the #expression is called a boolean expression


 # Practice

test_dict = {
    'link1': {'peer': '192.168.1.10', 'local': '10.0.0.10', 'interface': '2068'},
    'link2': {'peer': '192.168.1.11', 'local': '10.0.0.11', 'interface': '2067'},
    'link3': {'peer': '192.168.1.12', 'local': '10.0.0.12', 'interface': '1403'},
    'link4': {'peer': '192.168.1.14', 'local': '10.0.0.17', 'interface': '1065'},
    'link5': {'peer': '192.168.1.15', 'local': '10.0.0.14', 'interface': '3029'},
    'link6': {'peer': '192.168.1.13', 'local': '10.0.0.19', 'interface': '2206'},
    'link7': {'peer': '192.168.1.18', 'local': '10.0.0.21', 'interface': '2173'},
    'link8': {'peer': '192.168.1.9', 'local': '10.0.0.25', 'interface': '1948'},
    'link9': {'peer': '192.168.1.19', 'local': '10.0.0.13', 'interface': '1429'},
    'link10': {'peer': '192.168.1.20', 'local': '10.0.0.9', 'interface': '1834'}
}
# printing 2067 from the nested dictionary list through the key 'interface'
print(test_dict['link2'])
print(test_dict['link2']['interface'])
# listing  and printing the interface ID in the nested dictionary
interface_id = ['2067', '1403', '1065', '3029', '2206', '2173', '1948', '1429', '1834']
print(interface_id)
# sorting and printing the interface_id list in descending order
interface_id.sort(reverse=True)
print("descending order:", interface_id)


try and except in python can be use to print a user friendly error

like specifying an = 
except ValueError:
      print(that is a wrong input)

you can use a for loop to access item in a list, if the list is an input
   for number_of_days_element in user_input:
  

