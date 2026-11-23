#String Indexing
#[start : End : step]
# by default step is set to +1 which moves from left to right
# start and end would be included in the output and 0 as step throws an error
phone = "9653520506"
print(phone[1:5])    #6535 would be the output
print(phone[:5:2])   # alternating numbers would get printed strting from 0 index to 5th i.e. 955
print(phone[-1:-5])  # negative sign start indexing from the last but step index is positive, so empty output
print(phone[::-1]) # now it reverses the string