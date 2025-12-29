num = int(input("Enter a number:"))

def fact_num(num):
    if num == 1:
        return 1
    else:
        fact = num * fact_num(num-1)
        return fact
print(f"Factorial of {num} is {fact_num(num)} ")
