from utils import get_sum, get_product

def show_result(x, y, operation = "sum"):

    if operation == "sum":
        print("The result is: ",  get_sum(x,y))
    else:
        print("The result is:", get_product(x,y))

if __name__ == "__main__":
    x = int(input("Enter first number"))
    y = int(input("Enter second number"))
    operation = input("Enter 1 for Sum & 2 for Product")

    show_result(x,y, operation)