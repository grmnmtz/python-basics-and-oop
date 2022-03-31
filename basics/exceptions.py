# How to raise and handle exceptions.

# Raising exceptions, very useful in functions and OOP.

# raise Exception("Bad timing")

# raise FileExistsError("File already exists.")

try:
    x = 7 / 0
except Exception as e: # access the exception as e variable
    print(e)
finally: # always executed at the end.
    print("Cleaning operations.")

