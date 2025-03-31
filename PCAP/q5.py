# How many stars (*) does the following snippet print?
i = 10
while i > 0 :
    i -= 3
    print("*")
    if i <= 3:
        break
else:
    print("*")

# i = 10
# ↓ (i > 0? Yes)
# i = 10 - 3 = 7 → print("*") → i <= 3? No
# ↓
# i = 7 - 3 = 4 → print("*") → i <= 3? No
# ↓
# i = 4 - 3 = 1 → print("*") → i <= 3? Yes → BREAK
# No else block execution because the loop broke.

# Total stars: 3.