vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def shorten(word):
    for vowel in vowels:
        word = word.replace(vowel, "") #remove vowels

    return word

    #In each iteration, vowel is assigned to the element from the vowels list
    # In the first iteration, vowel = 'a'
    # In the second iteration, vowel = 'e':
    # In the third iteration, vowel = 'i':
    # In the fourth iteration, vowel = 'o'
    # In the fifth iteration, vowel = 'u'.
    #For each vowel, replace() is called, replacing all occurrences of that vowel

def main():
    word=input("Input: ")
    text=shorten(word)
    print(text)

if __name__ == "__main__":
    main()
