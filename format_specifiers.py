# Format specifiers are used to align, present your text in a clean manner
# {value : flags} values are formatted on the basis of flags inserted

a = 3.14159
b = -955.389
c = 300325

print(f"value of a {a:>+.2f}") # < -> right alignment, > -> left allignment , ^ -> centre allignment
print(f"value of a {b:>+.2f}") # + -> for signifying positive values, .2f -> for specifying two decimal places 
print(f"value of a {c:>+,.2f}") # , -> for sseparating thousands in a number
