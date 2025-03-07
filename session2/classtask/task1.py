# class task 1
# take the word input (strind)
# find the length of the word
# id the length is more than 10
# print('THAT'S A LONG WORD. IT HAS {length of the word} characters')
# else
# print ('the word has {length of the word} characters')

sentence = input("Provide a sentence please: ")
length =  len(sentence)
if length > 10:
    print(f'THAT\'S A LONG WORD. IT HAS {length} characters')
else:
    print(f'the word has {length} characters')


# f-string: The f before the string allows you to directly embed expressions inside curly braces {}cod