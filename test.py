largest = None
smallest = None

while True:
    sval = input("Enter a number: ")
    if sval == "done" :
        break
    try:
        fval = float(sval)
        if smallest is None:
            smallest = fval
        elif smallest > fval:
            smallest = fval
        else:
            smallest = smallest
            if largest is None:
                largest = fval
            elif largest < fval:
                largest = fval
    except:
        print("Invalid Input")
        continue


print("Maximum is", largest)
print("Minimum is", smallest)
