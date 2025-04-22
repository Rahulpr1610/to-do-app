date = input("Enter a date : ")
mode = input("Enter today's your mood's : ")
thoughts = input("Enter your today's mode : ")

with open(f"../jonour/{date}.txt", "w") as file:
    file.write(mode + 2* '\n')
    file.write(thoughts)
