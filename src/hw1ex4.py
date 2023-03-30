import sys


def compare_fruits(user_input):
    my_favorite_fruits = ["apple","orange", "kiwi", "berries", "melon", "cucumber", "carrot", "watermelon","potato",
                          "cabbage"]
    for item in user_input:
        for item1 in my_favorite_fruits:
            if item == item1:
                print("That is my " + str(my_favorite_fruits.index(item1)+1) + "th favorite fruit")
            else:
                "ooh good choice"


def main():
    fruit_choice = input("What is your favorite fruit? \n")
    user_list = fruit_choice.split()
    compare_fruits(user_list)


if __name__ == "__main__":
    sys.exit(main())
