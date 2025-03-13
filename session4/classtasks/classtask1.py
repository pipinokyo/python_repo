inp_char = input('Please provide a character: ')

lst_names = [
    "Esen",
    "Beka",
    "Iana",
    "Erkin",
    "Aigerim",
    "Kostya",
    "Jyldyz",
    "Cuneyt",
    "Gulnaz",
    "Aibek",
]
found = False  
for name in lst_names:
    if inp_char.lower() in name.lower():
        print(name)
        found = True  
if not found:
    print(f'no student that has letter {inp_char}')
    