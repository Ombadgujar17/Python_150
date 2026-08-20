word=input("Enter a word: ")
word=word.lower()
if word[0] in "aeiou":
    new_word=word[0:]+"way"
    print(new_word)
else:
    new_word=word[1:]+word[0]+"ay"
    print(new_word)