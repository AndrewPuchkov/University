import os
import pdf2docx
from pdf2docx import *
import docx2pdf
from docx2pdf import *
import PIL
from PIL import Image

cwd = os.getcwd()
print(cwd)


def change_catalog(path: str) -> str:
    os.chdir(path)
    return os.getcwd()


def change_pdf2docx(path: str) -> None:
    pdf_file = path
    docx_file = path[:-3] + 'docx'
    parse(pdf_file, docx_file)


def change_docx2pdf(path: str) -> None:
    convert(path)


def compression_image(path: str, compression_k: int) -> None:
    image_file = Image.open(path)
    image_file.save(f"new {path}", quality=compression_k)


def pdf_in_directory() -> list:
    print('Список файлов с расширением PDF в данном каталоге')
    list_with_pdf = [i for i in os.listdir(path='.') if i[-4:] == '.pdf']
    return list_with_pdf


def docx_in_directory() -> list:
    print('Список файлов с расширением Docx в данном каталоге')
    list_with_docx = [i for i in os.listdir(path='.') if i[-5:] == '.docx']
    return list_with_docx


def images_in_directory() -> list:
    print('Список файлов с расширением "jpeg","jpg","gif","png" в данном каталоге')
    list_with_images = [i for i in os.listdir(path='.') if
                        i[-5:] == '.jpeg' or i[-4:] == '.jpg' or i[-4:] == '.gif' or i[-4:] == '.png']
    return list_with_images


def files_with_start(start_str: str) -> list:
    list_with_start = [i for i in os.listdir(path='.') if i.startswith(start_str)]
    return list_with_start


def files_with_end(end_str: str) -> list:
    list_with_end = [i for i in os.listdir(path='.') if i.split('.')[-2].endswith(end_str)]
    return list_with_end


def files_with_str(str: str) -> list:
    list_with_str = [i for i in os.listdir(path='.') if str in i]
    return list_with_str


def files_with_expansion(expansion: str) -> list:
    list_with_expansion = [i for i in os.listdir(path='.') if i.endswith(expansion)]
    return list_with_expansion


def chosen1():
    list_with_pdf = pdf_in_directory()
    for i in range(len(list_with_pdf)):
        print(f"{i + 1}. {list_with_pdf[i]}")
    print()
    number_pdf = input(('Введите номер файла для преобразования в Docx (чтобы преобразовать всё, введите 0; для отмены -1): ')).strip()
    if number_pdf == '0':
        for i in range(len(list_with_pdf)):
            change_pdf2docx(list_with_pdf[i])
    elif number_pdf == '-1':
        print()
    else:
        change_pdf2docx(list_with_pdf[int(number_pdf) - 1])
    print(f'Преобразование файла {list_with_pdf[int(number_pdf) - 1]} из PDF в Docx прошло успешно!')


def chosen2():
    list_with_docx = docx_in_directory()
    for i in range(len(list_with_docx)):
        print(f"{i + 1}. {list_with_docx[i]}")
    print()
    number_docx = (input(('Введите номер файла для преобразования в PDF (чтобы преобразовать всё, введите 0; для отмены -1): ')))
    if number_docx == '0':
        for i in range(len(list_with_docx)):
            change_pdf2docx(list_with_docx[i])
    elif number_docx == '-1':
        print()
    else:
        change_docx2pdf(list_with_docx[int(number_docx) - 1])
    print(f'Преобразование файла {list_with_docx[int(number_docx) - 1]} из Docx в PDF прошло успешно!')


def chosen3():
    list_with_images = images_in_directory()
    for i in range(len(list_with_images)):
        print(f"{i + 1}. {list_with_images[i]}")
    print()
    number_images = int(input(('Введите номер файла для сжатия (чтобы сжать всё, введите 0, для отмены -1): ')))
    compression_k = int(input('Введите на сколько надо сжать изображение от 0 до 95: '))
    if number_images == 0:
        for i in range(len(list_with_images)):
            compression_image(list_with_images[i], compression_k)
    elif number_images == '-1':
        print()
    else:
        compression_image(list_with_images[int(number_images) - 1], compression_k)


def delete_file(path: str) -> None:
    if os.path.isfile(path):
        os.remove(path)
    else:
        for root, dirs, files in os.walk(path, topdown=False):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                os.rmdir(os.path.join(root, dir))
        os.rmdir(path)


def delete(path: str) -> bool:
    if not os.path.exists(path):
        return False
    delete_file(path)
    return True


def deleted(choose_for_delete: str) -> None:
    if choose_for_delete == '1':
        start_str = input('Введите начало строки, с которой хотите удалить файл: ')
        fws = files_with_start(start_str)
        for i in fws:
            delete(i)
    elif choose_for_delete == '2':
        end_str = input('Введите конец строки, с которой хотите удалить файл: ')
        fwe = files_with_end(end_str)
        for i in fwe:
            delete(i)
    elif choose_for_delete == '3':
        str = input('Введите подстроку, с которой хотите удалить файл: ')
        fwstr = files_with_str(str)
        for i in fwstr:
            delete(i)
    elif choose_for_delete == '4':
        expansion = input('Введите расширение, с которым хотите удалить файлы: ')
        fwexpansion = files_with_expansion(expansion)
        for i in fwexpansion:
            delete(i)


def chosen4():
    print('1. Удалить все файлы, начинающиеся на определенную подстроку')
    print('2. Удалить все файлы, заканчивающиеся на определенную подстроку')
    print('3. Удалить все файлы, содержащие определенную подстроку')
    print('4. Удалить все файлы по расширению')
    choose_for_delete = input('Введите номер команды: ')
    deleted(choose_for_delete)


'''def interface_directory():
    flag = True
    while flag != False:
        print('Выберите действие: ')
        print('0. Сменить рабочий каталог')
        print('1. Преобразовать PDF в Docx')
        print('2. Преобразовать Docx в PDF')
        print('3. Произвести сжатие изображений')
        print('4. Удалить группу файлов')
        print('5. Выход')
        choose = input('Выберите действие: ')
        if choose == '0':
            catalog = input('Введите абсолютный путь каталога: ')
            print(f"Текущий каталог: {change_catalog(catalog)}")
        elif choose == '1':
            chosen1()
        elif choose == '2':
            chosen2()
        elif choose == '3':
            chosen3()
        elif choose == '4':
            chosen4()
        elif choose == '5':
            flag = False
        else:
            print('Вы ошиблись, введите номер команды ещё раз')'''
