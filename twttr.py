text=input("Input: ")
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for vowel in vowels:
    #In each iteration, vowel is assigned to the element from the vowels list

    # In the first iteration, vowel = 'a'
    # In the second iteration, vowel = 'e':
    # In the third iteration, vowel = 'i':
    # In the fourth iteration, vowel = 'o'
    # In the fifth iteration, vowel = 'u'.

    text = text.replace(vowel, "")
    #For each vowel, replace() is called, replacing all occurrences of that vowel

print(text)
