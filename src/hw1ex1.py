import sys


def evaluate_user_input(user_input):
    my_favorite_food_list = ["apple", "orange", "banana"]
    if user_input == my_favorite_food_list[0]:
        print("Mine too!")
    elif user_input == my_favorite_food_list[1]:
        print("That is my second favorite!")
    else:
        print("Ooh good choice")


def main():
    fruit_choice = input("What is your favorite fruit? enter one fruit only: \n")
    # make sure all characters are in lower case
    fruit_choice_lower_case = fruit_choice.lower()
    evaluate_user_input(fruit_choice_lower_case)


if __name__ == "__main__":
    sys.exit(main())

