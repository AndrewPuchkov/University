def inf(file):
    with open(file, mode='r', encoding='utf-8') as text:
        strings = text.read().splitlines()
    split_strings = [x.split('|') for x in strings]
    return split_strings


split_strings = (inf('info.csv'))

def get_books(word, split_strings):
    for string in split_strings:
        for strings in string:
            if word in strings:
                print(string)


get_books('Python', split_strings)
