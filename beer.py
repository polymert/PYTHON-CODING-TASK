import time

# The time module is used to get the current time and to format it to a string.
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
# The current time is checked to see if it is between 4pm and 6pm.
if current_time >= "04:00:00" and current_time <= "18:00:00":
    print("Current time is:", current_time, "No beer before 4pm o’clock\n")
else:
    print("Current time is:", current_time, "It's time for a beer\n")
    i = 99
    # The script starts with 99 bottles of beer on the wall.
    while i > 0:
        print(i, "bottles of beer on the wall.")
        print(i, "bottles of beer.")
        print("Take one down and pass it around,")
        print(i - 1, "bottles of beer on the wall.\n")

        # Prompts the user to take another bottle down with allowed answers
        answer = input("Take another down? Allowed answers are “yes”, “y”, “no”, “n”: ")
        if answer == "yes" or answer == "y":
            print("")
            # If the user chooses to take another bottle down, the count decreases.
            i -= 1
        elif answer == "no" or answer == "n":
            print("")
        else:
            print("The answer was an unallowed one.\n")

        # If the count reaches 0, the script prompts the user to buy more bottles.
        if i == 0:
            print("No more bottles of beer on the wall,")
            print("no more bottles of beer.\n")
            input("Buy some more? Press a button to get some more\n")
            # The count is reset to 99 and the script starts over.
            i = 99
            print(
                "Go to the store and buy some more, 99 bottles of beer on the wall..."
            )
