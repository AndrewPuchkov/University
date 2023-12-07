import file_change
import os

def show():
    return '1. Преобразовать PDF в Docx\n2. Преобразовать Docx в PDF\n3. Произвести сжатие изображения\n4. Удалить файлов'


def show_method(file, flag=False):
    arr = set([i.split('.')[-1] for i in file])
    if len(arr) == 1:
        arr = list(arr)[0]
        if arr == 'jpg' or arr == 'png' or arr == 'jpeg':
            if flag:
                file_change.chosen3(file)
                return f"Сжатие изображения {' '.join(file)} прошло успешно!"
            return 'Произвести сжатие изображений'
        elif arr == 'pdf':
            if flag:
                file_change.chosen1(file)
                return f"Преобразование файла {' '.join(file)} в каталоге из PDF в Docx прошло успешно!"
            return 'Преобразовать PDF в Docx'
        elif arr == 'docx':
            if flag:
                file_change.chosen2(file)
                return f"Преобразование файла {' '.join(file)} в каталоге из Docx в PDF прошло успешно!"
            return 'Преобразовать Docx в PDF'
    else:
        return 'Ты долбаеб'

def Del(file):
    os.remove(file[0])
    return 'Файл удален'
