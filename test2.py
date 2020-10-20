largest = None
smallest = None

while True:
    try:
        value = input("Enter a number: ")
        if value == "done" :
            break
        else:
            istr = int(value)
            print("value",value)
            continue

        if value > smallest:
            smallest = smallest
        elif value < smallest:
            smallest = value
            print("value2")
            break
        else:
            continue

    except:
        print("Invalid Input")

print("Maximum is", largest)
print("Minimum is", smallest)
