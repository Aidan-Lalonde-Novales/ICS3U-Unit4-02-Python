#!/usr/bin/env python3

# Created by Aidan Lalonde-Novales
# Created April 2022
# This program tells the user the factorial of the number they entered.


def main():
    # this function calculates factorials
    counter = 1
    sum_count = 1

    # input
    times_to_loop_string = input("Please enter a positive integer: ")

    # process & output
    try:
        times_to_loop = int(times_to_loop_string)

        if times_to_loop >= 0:
            while counter <= times_to_loop:
                sum_count = sum_count * counter
                counter = counter + 1
            print("The factorial of {0} is {1}.".format(times_to_loop, sum_count))
        else:
            print("Please input a positive integer.")

    except Exception:
        print("Your integer is invalid! Please try again.")

    print("\nDone.")


if __name__ == "__main__":
    main()
