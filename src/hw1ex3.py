import sys


def main():

    flowers = {"Sara": "Daffodil", "Phillip": "Gardenia", "William": "Honeysuckle", "Irena": "Marigold"}
    print("part a:")
    flowers.get("Phillip")
    print(flowers)
    print("part b:")
    new_value = {"Irena": "Lilac"}
    flowers.update(new_value)
    print(flowers)
    print("part c:")
    flowers.pop("William")
    print(flowers)
    print("part d:")
    flowers["Timothy"] = "Lavender"
    print(flowers)
    

if __name__ == "__main__":
    sys.exit(main())




