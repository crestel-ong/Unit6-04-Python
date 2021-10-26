#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: Oct 2021
# this is the average of 2d array program in python
# this program uses a 2d array

import random


def average_of_numbers(passed_in_2D_list):
    # this function calculates the average of the elements in an 2D array

    # delcaring
    total = 0
    average = 0

    for row_value in passed_in_2D_list:
        for single_element in row_value:
            total += single_element

    amount_of_numbers = len(passed_in_2D_list) * len(row_value)
    average = total / amount_of_numbers

    return average


def main():
    # this function uses a 2D array

    a_2d_list = []

    # input
    row_as_string = input("How many rows would you like: ")
    column_as_string = input("How many columns would you like: ")
    print(" ")

    try:
        # covert from string to float
        rows = int(row_as_string)
        columns = int(column_as_string)
        for loop_counter_rows in range(0, rows):
            temp_column = []
            for loop_counter_columns in range(0, columns):
                a_random_number = random.randint(1, 50)
                temp_column.append(a_random_number)
                print("{0} ".format(a_random_number), end="")
            a_2d_list.append(temp_column)
            print("")

        average_of_numb = average_of_numbers(a_2d_list)
        rounded_average_number = round(average_of_numb, 2)
        print(
            "\nThe average of all the numbers is: {0} ".format(rounded_average_number)
        )

    except Exception:
        print("Invalid input.")
    print("\nDone.")


if __name__ == "__main__":
    main()
