sentence = input("Enter a sentence: ")

vowel_map = {
    'a': '1',
    'e': '2',
    'i': '3',
    'o': '4',
    'u': '5'
}

transformed = ""

for char in sentence:
    if char.lower() in vowel_map:
        transformed += vowel_map[char.lower()]
    else:
        transformed += char

print(f"Transformed sentence: {transformed}")
