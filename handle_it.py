#handle it
#shows how to handle exceptions

#try/except
try:
    num = float(input('Enter a number: '))
except:
    print('something went wrong!')

#specifying exception type
try:
    num = float(input("\nEnter a number: "))
except ValueError:
    print("That was not a number")
    #common exception types:
    #IOError, IndexError, KeyError, NameError, SyntaxError, TypeError
    #ValueError, ZeroDivisionError

#handle multiple exception types
print()
for value in (None, "Hi!"):
    try:
        print("Attempting to convert", value, "-->", end=" ")
        print(float(value))
    except (TypeError, ValueError):
        print("Something went wrong!")

#get an exceptions argument
try:
    num = float(input("\nEnter a number: "))
except ValueError as e:
    print("That was not a number! Or as python would say...")
    print(e)

#try/except/else
try:
    num = float(input("\nEnter a number: "))
except ValueError:
    print("That was not a number!")
else:
    print("you entered the number!", num)

input("\n\nPress the enter key to exit.")
