#!/usr/bin/env python3

# Created by Marwan Mashaly
# Created on October 2019
# This program tells the user if he can have a raise of 5% or no


def main():
    # This function tells the user if he can have a raise of 5% or no

    # input
    years_of_service = input("Enters years of service at the company: ")
    salary = input("Enter your current salary: ")
    print("")

    # process & output
    try:
        service = int(years_of_service)
        salary_check = int(salary)

        if service >= 5:
            bonus = 0.05 * salary_check
            total = bonus + salary_check
            print("your new salary is", total)
        else:
            print(" Sorry, you can't have a raise")
    except Exception:
        print("Invalid years of service or salary_check")

    finally:
        print("")
        print("Thanks for trying")


if __name__ == '__main__':
    main()
