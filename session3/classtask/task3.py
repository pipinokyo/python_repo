# character counter
# take an input of the word/sentence
# calculate how many 'a' character are in the word/sentence

# sentence = str.lower(input("input: "))
# word = str.lower(input('which character do want me to count: '))
# counter = 0
# for letter in sentence:
#     if letter == word:
#         counter = counter + 1
# print(counter)



# another 
sentence = input("input: ").lower()
word = input('which character do want me to count: ').lower()
word2 = input('which second character do want me to count: ').lower()
counter = 0
counter2 = 0
if len(word) == 1 and len(word2) == 1:
    
    for letter in sentence:
        if letter == word:
            counter = counter + 1
        elif letter == word2:        
            counter2 = counter2 + 1

    print(f"{word} = {counter}")
    print(f"{word2} = {counter2}")
else:
    print('character input is more than 1')
