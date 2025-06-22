#len()method
str1="hello world"
a=len(str1)
print(a)
#title()
str1="hello World"
a=str1.title()
print(a)
#lower()
str1="HELLO WORLD"
a=str1.lower()
print(a)
#upper()
str1="hello world"
a=str1.upper()
print(a)
#count(str.start.end)
str1="hello world!hello hello"
a=str1.count('hello')
print(a)
#find(str.start.end)
str1="hello world!hello hello"
a=str1.find('hello')
print(a)
#index
str1="Hello world!hello hello"
a=str1.index('hello')
print(a)
#endswith()
str1="hello world"
a=str1.endswith("world")
print(a)
#startswith()
str1="hello world"
a=str1.startswith('he')
print(a)
#isalnum()
str1="Hello world"
a=str1.isalnum()
print(a)
#isspace()
str1='\n \t \e'
a=str1.isspace()
print(a)
#islower()
str1="hello world"
a=str1.islower()
print(a)
#isupper()
str1="HELLO WORLD"
a=str1.isupper()
print(a)
#istitle()
str1="Hello world"
a=str1.istitle()
print(a)
#lstrip()
str1="  Hello world"
a=str1.lstrip()
print(a)
#rstrip()
str1="Hello world  "
a=str1.rstrip()
print(a)
#strip()
str1="  hello world  "
a=str1.strip()
print(a)
#replace(oldstr.newstr)
str1="hello world"
a=str1.replace('o','*')
print(a)
#join()
str1=("hello world!")
str2='-'
a=str2.join(str1)
print(a)