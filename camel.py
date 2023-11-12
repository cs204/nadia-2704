camelCase = input('Верблюжий стиль: ')
snakeСase = ''

for letter in camelCase:
 if letter.isupper():
    snakeСase += "_" + letter.lower()
 else:
    snakeСase += letter

print(snakeСase)