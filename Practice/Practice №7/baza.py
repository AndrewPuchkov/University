def inf(file):
    with open(file, mode='r', encoding='utf-8') as text:
        strings = text.read().splitlines()
    split_strings = [x.split('|') for x in strings]
    return split_strings


def get_books(word, split_strings):
    search_list = []
    for string in split_strings:
        for strings in string:
            if word in strings:
                search_list.append(string)
    return search_list


def get_total(list):
    number_price_of_search_list = []
    for element in list:
        if (int(element[3]) * float(element[4])) < 500:
            number_price_of_search_list.append((element[0], int(element[3]) * float(element[4]) + float(100)))
        else:
            number_price_of_search_list.append((element[0], int(element[3]) * float(element[4])))
    #number_price_of_search_list = [(x[0], int(x[3]) * float(x[4])) for x in list]
    return number_price_of_search_list
