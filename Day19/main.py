from calculator.operations import add, subtract, multiply, divide

def main():
    print("Addition:", add(10, 5))
    print("Subtraction:", subtract(10, 5))
    print("Multiplication:", multiply(10, 5))
    try:
        print("Division:", divide(10, 0))
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()