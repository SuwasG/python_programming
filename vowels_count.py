userInput = input("Enter a sentence/string: ")

def count_vowels(string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

vowel_count = count_vowels(userInput)
print(vowel_count)


# method 2 using generator expression
userInput = input("Enter a sentence/string: ").lower()

def count_vowels(string):
    vowels = set('aeiou')  # Using a set for vowels
    count = sum(1 for char in string if char in vowels)  
    # counts how many times a character in string passes the if char in vowels test. For each such character, a 1 is generated, and then all these 1s are added together by sum, resulting in the total count of vowels in the string.
    return count

vowel_count = count_vowels(userInput)
print(vowel_count)
