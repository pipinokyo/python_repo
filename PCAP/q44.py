# What is the expected output of the following code?

plane = "Cessna"
counter = 0
for c in plane * 2:
    if c in ["e", "a"]:
        counter += 1
print(counter)