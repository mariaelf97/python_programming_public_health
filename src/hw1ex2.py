import sys


def main():
    animals = ["Zebra", "Lion", "Possum", "SealLion", "Panda", "Elephant", "Cheetah"]
    print("Question 2 part a:")
    print(dir(animals))
    print("Question 2 part b:")
    animals.append("sloth")
    print(animals)
    print("Question 2 part c:")
    animals.remove("Possum")
    print(animals)
    print("Question 2 part d:")
    print(len(animals))
    print("Question 2 part e:")
    print(list(reversed(animals)))


if __name__ == "__main__":
    sys.exit(main())

