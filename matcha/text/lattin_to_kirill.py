import re

def find_abbreviations(text):
    # Используем регулярное выражение для поиска аббревиатур на латинице
    abbreviations = re.findall(r'\b[A-ZА-Я]{1,7}(?:[\'-][A-ZА-Я]{1,7})*\b', text)
    return abbreviations

def replace_latin_abbreviations(abbreviation, letter_dict):
    # Заменяем каждую букву в аббревиатуре на её представление в виде слова
    for letter, word in letter_dict.items():
        abbreviation = abbreviation.replace(letter, word)
    return abbreviation

# Пример использования

def replace_latin_with_cyrillic(text):
    latin_cyrillic_mapping = {
        'a': 'а', 'b': 'б', 'c': 'ц', 'd': 'д', 'e': 'е', 'f': 'ф', 'g': 'г', 'h': 'х', 'i': 'и',
        'j': 'й', 'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о', 'p': 'п', 'q': 'кыю', 'r': 'р',
        's': 'с', 't': 'т', 'u': 'у', 'v': 'в', 'w': 'в', 'x': 'х', 'y': 'ы', 'z': 'з',
        'A': 'А', 'B': 'Б', 'C': 'Ц', 'D': 'Д', 'E': 'Е', 'F': 'Ф', 'G': 'Г', 'H': 'Х', 'I': 'И',
        'J': 'Й', 'K': 'К', 'L': 'Л', 'M': 'М', 'N': 'Н', 'O': 'О', 'P': 'П', 'Q': 'Кыю', 'R': 'Р',
        'S': 'С', 'T': 'Т', 'U': 'У', 'V': 'В', 'W': 'В', 'X': 'Х', 'Y': 'Ы', 'Z': 'З',
        'ch': 'ч', 'sh': 'ш', 'zh': 'ж', 'wh': 'в','th':'з','ch':'ч','sh':'ш','zh':'ж','Ck':'к','Kn':'н',
        'Ch': 'Ч', 'Sh': 'Ш', 'Zh': 'Ж', 'Wh': 'В','Th':'з','Ch':'ч','Sh':'ш','Zh':'ж','сk':'к','kn':'н'
    }

    result = ''
    i = 0
    while i < len(text):
        # Check for multi-letter combinations first
        for length in range(2, 0, -1):
            substr = text[i:i+length]
            if substr in latin_cyrillic_mapping:
                result += latin_cyrillic_mapping[substr]
                i += length
                break
        else:
            # If no match found, handle single characters
            result += latin_cyrillic_mapping.get(text[i], text[i])
            i += 1

    return result
# Словарь с соответствиями для замены букв в аббревиатурах и их представлений в виде слов
letter_dict = {
    'A': 'эй', 'B': 'би', 'C': 'си', 'D': 'ди', 'E': 'и', 'F': 'эф', 'G': 'джи', 'H': 'эйч',
    'I': 'ай', 'J': 'джей', 'K': 'кей', 'L': 'эл', 'M': 'эм', 'N': 'эн', 'O': 'оу', 'P': 'пи',
    'Q': 'кию', 'R': 'ар', 'S': 'эс', 'T': 'ти', 'U': 'ю', 'V': 'ви', 'W': 'ви', 'X': 'экс',
    'Y': 'вай', 'Z': 'зи'
}

# Находим аббревиатуры в тексте
def english_to_russian(text):

  abbreviations_found = find_abbreviations(text)

    # Заменяем буквы в каждой аббревиатуре
  replaced_abbreviations = {abbreviation: replace_latin_abbreviations(abbreviation, letter_dict) for abbreviation in abbreviations_found}

    # Заменяем аббревиатуры в тексте
  for abbreviation, replacement in replaced_abbreviations.items():
      text = text.replace(abbreviation, replacement)


  result = replace_latin_with_cyrillic(text)
  return result







