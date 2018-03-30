word = input("Enter word to check: ")

if str(word) == str(word)[::-1]:
    print("{} is a palindrome".format(word))
else:
    print("{} is not a palindrome".format(word))
