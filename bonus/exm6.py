feet_inches = input("Enter feet and inches : ")


def convert(feet_inches):

    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    meter = feet * 0.234 + inches * 0.234
    return f"{feet} feet and  {inches} inches os equal to {meter} meters . "

print(convert(feet_inches))