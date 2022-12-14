import re
txt=input("Enter a word to qualify")
#Chekc if the string has  any a, r , or n characters:
x=re.findall("[arn]",txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print('No match')

#[a-m] Returns a match ror any lower case character, alphabetically between a and
txt="the rain in Spain"
#heck if the string has any haracters between a and n:
x=re.findall("[a-n]",txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

#[^arn] Returna match for any character EXCEPT  a, r, and n
txt="The rain in spain"
#ChCheck if the string has other characters than a, r, or n:
x=re.findall("[^arn]",txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

#[0123] Returns a match where any of the spcified digits (0,1,2,3,) are represented
txt="The rain in Spain12"
#Check if the string has only 0,1,2,3 digits:
x=re.findall("[0123]",txt)
print(x)
if x:
    print("Yes, htere is at least match")
else:
    print("No match")

#[0-9] Returns a match for any diigit between 0 and 9
txt="Before 12:30 PM"
#Check if the stirng has nay digits:
x=re.findall("[0-9]",txt)
print(x)
if x:
    print("Yes, there is at least on match!")
else:
    print("No match")

# [0-5][0-9] Returns a match for any git number from 00 and 59

txt="Before 12:30 PM"

x=re.findall("[0-5][0-9]",txt)
print(x)
if x:
    print("yes, there is at least one match!")
else:
    print("No match")

# [a-z][A-Z] Returns a match for anyy character alphabetically between a and z , lower
txt="Before 12:30 PM"
# Check if the string has any characters from a to z
# lower case, and A to Z upper case:
x=re.findall("[a-z][A-Z]",txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")



# [+] In sets, +, *, ., |, (), $ , {} has no special meaning, so [+] means:
# return a match for any + character in the string

txt="Before 12:30 PM"
x=re.findall("[f.+e]",txt)
print(x)

if x:
    print("Yes,  there is at least one match!")
else:
    print("No match")

txt="The rain in Spain"
#Check if the stirng starts with "The":
x=re.findall("\AThe", txt)
print(x)
if x:
    print("Yes, there is a match!")
else:
    print("No match")

# \b Returns a match where the specified
# characters are a t the beginning or at the end  of a word

txt="The rain in Spain"
# Check if"aim" is present at the eginning of a WORD"

x=re.findall(r"\bain",txt)

print(x)
if x:
    print("Yes, there is match!")
else:
    print("No match")


txt="The rain in Spain"
#Check if "ain is present, but NOT  at the end of a word:
x=re.findall(r"ain\B",txt)
print(x)
if x:
    print('Yes, there is at least one match!')
else:
    print("No match")

# \D Returns a match where the string DOES NOT  contain digits
txt="the rain 24 in  Spain 56"
# Return a match at every no-digit character:
x=re.findall("\D",txt)
print(x)
if x:
    print("yes, ther is at least one match!")
else:
    print("No match")

#\s Return a match where the striing

# contains a whitespace character

txt="The rain in Spain"

#Return  a match at every white-space character"

x=re.findall("\s", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

#\w Returns a match where the s  contains

# any word characters
#and the underscore _ character

txt="the rin in _Spaiin$"
#Return a match at every word character (charcters from a to Z, digits from 0-9
x=re.findall("\w",txt)
print(x)
if x:
    print("yes, there is at least on match!")
else:
    print("No match")


#\W Returns a match wheret the stirng DOES  NOT contian any word characters
txt="The rain in Spain$"
# Return a match at every NON word character (characters NOT between a and Z .
x=re.findall("\W",txt)
print(x)

import re

mystring="Hello!! Good Morning Welcome to python tutorial class 24. For any queries please email to contactus@codetantra.com"
print(re.findall('^Hello',mystring))
print(re.findall('[0-9]+',mystring))
print(re.findall('[abc]+',mystring))
