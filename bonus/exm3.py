try:
    width = float(input("Enter the rectangle width : "))
    length = float(input("Enter the rectangle length : "))

    if width==length:
        exit("opps its looks like square")

    area = width*length

    print(area)
except ValueError:
    print("Enter a number ")