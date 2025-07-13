# Secret Castle game
print("\t\t\t\tA SECRET CASTLE\nWelcome to the game ")
print(":-You must enter the secret code to open the castle door\nCODE IS IN THREE DIGIT.")
print("Hint: The door only opens if the code is divisible by BOTH 3 and 5.\n")

life = 1

while life <= 3:
    code = int(input(f"Attempt {life}: Enter the secret code: "))

    if code <= 99 or code>=999 :
        print("Invalid input. Please enter a three digit no.")
        life += 1
        continue

    if code % 3 == 0 and code % 5 == 0:
        print("Access Granted! The door to the secret castle opens...")
        break
    elif code % 3 == 0:
        print("You are close! The code is divisible by 3.")
        life += 1
        continue
    elif code % 5 == 0:
        print("You are close! The code is divisible by 5.")
        life += 1
    else:
        print("Access Denied! This is not the correct code.")
        life += 1

if life > 3:
    print("\nOut of attempts. The castle remains locked.")