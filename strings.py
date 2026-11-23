# Learning and having familiarity with basic string operations
name = input("Enter your name : ")

print(len(name)) #outputs integer with the no. of characters in the (name) including spaces and characters

print(name.find("a")) #outputs the first occurence of the character

print(name.rfind("a")) #outputs the last occurence of the character
# if find and rfind can not identify the given character -> returns -1

print(name.capitalize()) #the First letter of the whole string is capitalized

print(name.upper(), name.lower()) #upper and lower case the whole string respectively

print(name.isdigit()) # returns boolean, TRUE -> if contains only digits, FALSE -> for the other conditions

print(name.isalpha()) # TRUE -> if string contains only alphabetical characters(no spaces allowed) , FALSE -> for any other cond

print(name.count("a")) #counts no. of characters in the string

print(name.replace("a","")) #replaces all a's with empty character -> removes all a's in the string

#String Indexing
#[start : End : step]
# by default step is set to +1 which moves from left to right
# start and end would be included in the output and 0 as step throws an error
phone = "9653520506"
print(phone[1:5])    #6535 would be the output
print(phone[:5:2])   # alternating numbers would get printed strting from 0 index to 5th i.e. 955
print(phone[-1:-5])  # negative sign start indexing from the last but step index is positive, so empty output
print(phone[::-1]) # now it reverses the string