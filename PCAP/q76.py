# What is the expected output of the following code?

vect = ["alpha", "bravo", "charlie"]
new_vect = filter(lambda s: s[-1].upper() in ["A", "O"], vect)
for x in new_vect:
    print(x[1], end="")


# Step-by-Step Evaluation:
# Define the list vect:
# vect = ["alpha", "bravo", "charlie"]
# Filter vect using filter and a lambda function:
# new_vect = filter(lambda s: s[-1].upper() in ["A", "O"], vect)
# The lambda function checks if the last character of a string (converted to uppercase) is either "A" or "O".
# Let's evaluate this for each string in vect:
# "alpha": Last character is 'a' → 'A' (after upper()). Is 'A' in ["A", "O"]? Yes → Included.
# "bravo": Last character is 'o' → 'O'. Is 'O' in ["A", "O"]? Yes → Included.
# "charlie": Last character is 'e' → 'E'. Is 'E' in ["A", "O"]? No → Excluded.
# So, new_vect will contain ["alpha", "bravo"] (filter object).
# Loop over new_vect and print the second character of each string:
# for x in new_vect: print(x[1], end="")
# x[1] refers to the second character (index 1) of each string in new_vect:
# "alpha": x[1] = 'l'
# "bravo": x[1] = 'r'
# end="" ensures no newline or space is added between characters.

# Final Output:
# The output will be the concatenation of the second characters of the filtered strings:
# lr

# Visualization:
# vect = ["alpha", "bravo", "charlie"]

# Filter condition: Last character is 'A' or 'O' (case-insensitive)
# - "alpha" → 'a' → 'A' → included
# - "bravo" → 'o' → 'O' → included
# - "charlie" → 'e' → 'E' → excluded

# new_vect = ["alpha", "bravo"]

# Loop:
# - "alpha"[1] = 'l'
# - "bravo"[1] = 'r'

# Output: 'l' + 'r' = "lr"