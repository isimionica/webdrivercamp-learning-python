#!/usr/bin/python3
def divide_safe(a, b):
    x = 0
    try:
        x = a / b
    except:
        x = None
    finally:
        print(f"Result: {x}")
    return (x)

if __name__ == "__main__":
    a = 9
    b = 3
    result = divide_safe(a, b)
    print(f"{a} / {b} = {result}")

    b = 0
    result = divide_safe(a, b)
    print(f"{a} / {b} = {result}")
