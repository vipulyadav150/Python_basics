while True:
    try:
        n=(int(input("Enter any number and know your chances of having a girlfriend?\n")))
        print(100/n)
        break
    except ValueError:
        print("Try again!I said a NUMBER!")
    except ZeroDivisionError:
        print("Hey! Lets omit 0!Try again!")
    finally:
        print("This is an example of Exception Handling!")





