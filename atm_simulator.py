correct_pin = "1212"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    pin = input("Enter your ATM PIN: ")

    if pin == correct_pin:
        print("Access Successful")
        break
    else:
        attempts += 1
        print(f"Wrong PIN Attempts left: {max_attempts - attempts}")

if attempts == max_attempts:
    print("Account Locked")