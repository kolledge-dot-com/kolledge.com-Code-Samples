# Control flow for if...elif...else statement

x = 15
if x > 25:
    print("I am the code-block-If")
    print("Logical-condition-if is True")
    print()
elif x > 20:
    print("I am the code-block-Elif-1")
    print("Logical-condition-if is False")
    print("Logical-condition-elif-1 is True")
    print()
elif x > 10:
    print("I am the code-block-Elif-2")
    print("Logical-condition-if is False")
    print("Logical-condition-elif-1 is False")
    print("Logical-condition-elif-2 is True")
    print()
else:
    print("I am the code-block-Else")
    print("Logical-condition-if is False")
    print("Logical-condition-elif-1 is False")
    print("Logical-condition-elif-2 is False")
    print()


print("I am the outer-code-block.")