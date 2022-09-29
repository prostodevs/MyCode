#! /usr/bin/env python3

def main():

    invalid = True
    while invalid:
        wordbank = ["indentation", "spaces"]
        tlgstudents = ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima",
                       "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

        # prompt for number and store in variable
        num = int(input(f"Please enter a number between 0 and {len(tlgstudents)-1}: "))
        # print(num)
        if (num >= 0 and num < len(tlgstudents)):
            # picks student from tlgstudents list based on user input
            student_name = tlgstudents[num]
            # print(student_name)
            # adds the integer 4 to wordbank list
            wordbank.append(4)
            invalid = False
        else:
            print("Sorry, that is not a vailid input.")

    # display a statement using user inputs
    print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")


main()
