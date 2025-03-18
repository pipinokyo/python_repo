# Task 2: Convert a Sentence to Abbreviations
# Write a function that takes a sentence as input and returns an abbreviation using the first letter of each word in uppercase.
# Example:
# print(abbreviate("Central Processing Unit"))

# Output:
# "CPU"


def abbreviate(whole_sentence): # We define a function named abbreviate that takes one parameter: whole_sentence (a string).
    each_word = whole_sentence.split() # The split() method splits the whole_sentence string into a list of words based on spaces.
    # after split() method each_word = ["Central", "Processing", "Unit"]
    first_letter = ""  # We create an empty string called first_letter to store the final abbreviation.
    for i in each_word:  # We use a for loop to iterate through each word in the each_word list.
        # In the first iteration, i = "Central". In the second iteration, i = "Processing".....
        abbreviation = i[0] # For each word (i), we extract the first character using indexing (i[0])
        # For i = "Central", abbreviation = "C". For i = "Processing", abbreviation = "P"....
        upper_case = abbreviation.upper() # We convert the extracted first letter to uppercase using the upper() method.
        first_letter += upper_case # We append the uppercase letter to the first_letter string.
    return first_letter # The function returns the first_letter string, which now contains the abbreviation.
whole_sentence = "Central Processing Unit" # we could take an input for this 
result = abbreviate(whole_sentence) # The result is stored in the result variable.
print(result)