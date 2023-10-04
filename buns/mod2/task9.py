s = input().replace(' ', '')
vowels = 0
consonant = 0
checkLetter = 'аеёиоуыэюя'
for i in range(len(s)):
    if s[i] in checkLetter:
        vowels += 1
    else:
        consonant += 1
print(vowels, consonant)