import file_change
import os

'''def show(list1):
    list_doc = []
    arr = set([i.split('.')[-1] for i in list1])
    if 'pdf' in arr:
        list_doc.append('Преобразовать PDF в Docx\n')
    if 'docx' in arr:
        list_doc.append('Преобразовать Docx в PDF\n')
    if 'jpg' in arr or 'jpeg' in arr or 'png' in arr:
        list_doc.append('Произвести сжатие изображения\n')
    if len(arr) > 0:
        list_doc.append('Удаление файлов')
    return ''.join(list_doc)'''


'''def show(file, flag_button, flag_del, flag=False):
    list1 = []
    button = ''
    arr = set([i.split('.')[-1] for i in file])
    if len(arr) == 1:
        arr = list(arr)[0]
        if arr == 'jpg' or arr == 'png' or arr == 'jpeg':
            list1.append('Произвести сжатие изображений')
            button += 'Сжатие'
            flag_button = True
        elif arr == 'pdf':
            list1.append('Преобразовать PDF в Docx')
            button += 'PDF в Docx'
            flag_button = True
        elif arr == 'docx':
            list1.append('Преобразовать Docx в PDF')
            button += 'Docx в PDF'
            flag_button = True
    if len(arr) > 0:
        list1.append('Удалить')
        flag_del = True
    return list1, flag_button, flag_del'''


def show(file, flag=None, koef=None):
    if not flag:
        list1 = []
        arr = set([i.split('.')[-1] for i in file])
        if len(arr) == 1:
            arr = list(arr)[0]
            if arr == 'jpg' or arr == 'png' or arr == 'jpeg':
                list1.append('Произвести сжатие изображений')
            elif arr == 'pdf':
                list1.append('Преобразовать PDF в Docx')
            elif arr == 'docx':
                list1.append('Преобразовать Docx в PDF')
        if len(arr) > 0:
            list1.append('Удалить')
        return list1
    if flag:
        if 'сжатие' in flag:
            file_change.chosen3(file, koef)
            return f"Сжатие изображения(-ий) прошло успешно!"
        elif 'PDF в Docx' in flag:
            file_change.chosen1(file)
            return f"Преобразование файла(-ов) в каталоге из PDF в Docx прошло успешно!"
        else:
            file_change.chosen2(file)
            return f"Преобразование файла(-ов) в каталоге из Docx в PDF прошло успешно!"


def delete(file):
    for i in range(len(file)):
        os.remove(file[i])
    return 'Файл(-ы) удален'
