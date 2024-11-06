# Write a program to simulate a simple ATM withdrawal system.


atm_balance = 1000
denominations = [100, 50, 20, 10]

amount = int(input("Enter the amount you want to withdraw: "))

if amount % 10 != 0:
    print("Please enter an amount that is a multiple of 10.")
else:
    notes = {}
    for denomination in denominations:
        notes[denomination] = amount // denomination
        amount %= denomination

    if amount == 0:
        print("Notes required:")
        for note, count in notes.items():
            if count > 0:
                print(f"${note} x {count}")
    else:
        print("ATM does not have enough cash.")
