print("Wel Come to Pig Latin!")
#apple in pig latin is ppleaay 
#ball in pig latin is allbay
#cat in pig latin is atcay
#dog in pig latin is ogday
#elephant in pig latin is lephanteay
#suwas in pig latin is uwasay etc.
pyg="ay"
original=input("Enter the word to be converted into Pig Latin: ")

if len(original)>0 and original.isalpha():
    
    word=original.lower()
    first=original[0]
else:
    print("Plz enter the word kindly next time ")
    quit()
new_word =word +first+pyg
new_word1=new_word[1:]

print(f"The pig latin of '{original}' is ",new_word1)