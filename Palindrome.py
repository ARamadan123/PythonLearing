# Checks if word is Palindrome
# A palindrome is the same word spelt backwards
# program will take user input and check

word = input("Enter String: ") # takes input

reversedWord = word[::-1] # Assigns reversed string

if word == reversedWord: # condition
    print(word + " is a palindrome")
    print("String: " + word)
    print("Reversed String: " + reversedWord)
else:
    print(word + " is not a palindrome")
    print("String: " + word)
    print("Reversed String: " + reversedWord)