def stripword(n, list1):
    for words in list1:
        words = words.strip()
    if n not in words:
        return False
    else:
        return n
print(stripword('hello', ['hey', 'good', '   hello   ']))