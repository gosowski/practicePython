def enterString():
    word = input("Enter string: ")
    return word

def reverseString(w):
    rev = w.split()
    return " ".join(rev[::-1])
    
phrase = enterString()
print(reverseString(phrase))

