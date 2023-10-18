import string


def countLetter(fileName):
    with open(fileName, 'r', encoding='utf-8') as file:
        content = file.read()
    letter_counts = {}
    for char in content:
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1

    sorted_counts = sorted(letter_counts.items(), key=lambda x: x[1])
    with open(fileName, 'w', encoding='utf-8') as file:
        for item in sorted_counts:
            file.writelines(f"{item[0]}: {item[1]}\n")


name = input()
filename = f"{name}.txt"
countLetter(filename)