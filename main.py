str_one = "Hi"
str_two = "there"

print("{0} {1}".format(str_one, str_two))

print("This program will join two parts of your text!")

while True:
    first = input("Enter the first part of your text: ")
    second = input("Enter the second part of your text: ")
    print("{0} {1}".format(first, second))

    end = input("Do you want to go again? ")
    if end.lower() == "no":
        break
