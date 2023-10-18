def countLetter(fileName):
    with open(fileName, 'r', encoding='utf-8') as file:
        content = file.read()
    letterCounts = {}
    for char in content:
        if char.isalpha():
            letterCounts[char] = letterCounts.get(char, 0) + 1
    sorted_counts = sorted(letterCounts.items(), key=lambda x: x[1])
    with open(fileName, 'w', encoding='utf-8') as file:
        for item in sorted_counts:
            file.writelines(f"{item[0]}: {item[1]}\n")

name = input()
filename = f"{name}.txt"
countLetter(filename)
