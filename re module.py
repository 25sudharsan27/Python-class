import re
txt="The rain in Spain"
#Find all lower case characters alphabetically between a and m"
x=re.findall("[a-m]",txt)
print(x)

#Find all digit characters:
#\d=Returns a match where the string contains digits(numbers from 0-9)
#\D=Returns a match where the string DOES NOT  contain digists

txt="That will be 59 dollars"
x=re.findall("\d",txt)
print(x)
x=re.findall("\D",txt)
print(x)
#.=. Anycharacer (except newline character)
txt="hello planet helo"
#Search for a sequency that starts with "he", followed gby two (any) character
x=re.findall("he..o",txt)
print(x)

#^ Starts with
txt="hello plant"
#Check if the string starts with 'hello':
x=re.findall("^hello",txt)
print()
if x:
    print("Yes, the stirng starts with 'hello'")
else:
    print("No Match")

#$ends wiith
txt="hello panet"
#Check if the string  ends with "planet":
x=re.findall("planet$",txt)
if x:
    print("Yes, the string ends with 'planet'")
else:
    print("No match")

# * =Zero or more ocurrences
txt="ruby rub rubyy"
#Search for a wequence that starts with "he", followed by  0 or more (any)
x=re.findall("ruby+",txt)
print(x)

txt="hello planet"
#Search for a sequence that starts with "he", followed by 0 or 1 (any)character
x=re.findall("he.?o",txt)
print(x)
#This time we got no mathch, because there were not zero , not one, but two characters

