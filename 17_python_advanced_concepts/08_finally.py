def divide(a,b):
    try: 
        c = a/b
        print(c)
        return c

    except Exception as e:
        print(e)
        return None

    # This is always executed no matter if try completely executes or not
    finally:
        print("this is always executed")

a = int(input("Enter a number 1: "))
b = int(input("Enter a number 2: "))
divide(a,b)