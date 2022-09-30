#!/usr/bin/env python3
""" Alta3 Research | J Stowe
    More Conditional Work """

def main():
    user_score = int(input("Please enter a number 1-100: "))
    if user_score >= 90:
        print("The score is A")
    elif user_score >=80:
        print("The score is B")
    elif user_score >= 70:
        print("The score is C")
    elif user_score >=60:
        print("The score is D")
    else: 
        print("The score is F")

if __name__ == "__main__":
    main()
