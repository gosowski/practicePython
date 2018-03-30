word = input("Enter word to check: ")

if str(word) == str(word)[::-1]:
    print("{} it is a palindrome".format(word))
else:
    print("{} it is not a palindrome".format(word))
