import os
os.system("clear")
print("Hello!")
print("=======================================================")
print("Demonstrating error handling.")
print("-------------------------------------------------------")

# =============== Function definition space ===============
def divide(a,b):
    try:
        return a/b
    except:
        return("Illegal division.")
# ============== End of Function Definition ===============

print("Please enter 2 numbers to divide.")
num1 = input("Dividend: ")
num2 = input("Divisor: ")
num1 = int(num1)
num2 = int(num2)
print(divide(num1,num2))
print()
