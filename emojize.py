#pip install emoji in command line

import emoji

def main():
    text=input("Input: ")
    emojitext=emoji.emojize(text, language='alias')
    print(emojitext)

main()
