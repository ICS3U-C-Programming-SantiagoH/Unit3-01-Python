#!/usr/bin/env python3
# Created by: Santiago Hewett
# Created on: Oct 11, 2023
# This program asks the user for the subtotal
# of a item and displays
# the subtotal, tax and total of tha item.

import constants


def main():
    # get the price of item
    print("This program will calculate the price of your item")
    print("with the subtotal of your item.")
    subtotal = float(input("Enter the subtotal of your item: "))

    # calculates the tax
    tax = subtotal * constants.HST

    # calculates the total
    total = subtotal + tax

    # display the subtotal
    print("")
    print("The subtotal of your item is = ${:.2f}".format(subtotal))

    # display the tax
    print("")
    print("The tax of your item is = ${:.2f}".format(tax))

    # display the total
    print("")
    print("The total of your item is = ${:.2f}".format(total))


if __name__ == "__main__":
    main()
