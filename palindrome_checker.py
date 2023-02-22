"""
hello_world_personal.py
"""


# A palindrome is a word or expression that reads the same forwards and backwards. "Eve" is a palindrome, as is "racecar." Typically capitalization, punctuation, and spacing aren't considered part of the expression, so "Madam in Eden, I'm Adam" is also a valid palindrome. Also: "A man, a plan, a canal: PANAMA!" Given that a palindrome has to include letters, the empty string "" is not a palindrome, although single letters like "e" are. Write a program palindrome_checker.py that includes a class definition for PalindromeChecker that includes at least two methods: a setter method setStrictMode() that takes a boolean value as input, which turns "strict mode" on and off a boolean method isPalindrome(phrase) that takes a phrase as a parameter and returns true if the phrase is a palindrome, and false if it isn't. This method should use a Deque object to check the expression, and return True if the expression entered is a valid palindrome. If "strict mode" is on, a palindrome will only be indicated if the phrase reads exactly the same, forwards and backwards, including spaces, punctuation, and case (upper and lower). If "strict mode" is off, then spaces, punctuation, and different cases are allowed, and the phrase will be identified as a palindrome because their letters all match. You may wish to write an additional helper method sanitize(phrase) that will produce a new, "sanitized" version of a phrase that doesn't have any spaces, punctuation, or uppercase letters in it. This method can be useful when "strict mode" is off. The main() function in the palindrome_checker.py can be used to perform a series of tests.


__author__ = "Hudson Stimmler"
__version__ = "2-22-2023"

from atds import Deque

def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.add_rear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.remove_front()
        last = chardeque.remove_rear()
        if first != last:
            stillEqual = False

    return stillEqual

def main():
    print(palchecker("lsdkjfskf"))
    print(palchecker("radar"))

if __name__ == "__main__":
    main()


