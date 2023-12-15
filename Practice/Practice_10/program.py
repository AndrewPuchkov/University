'''import PySimpleGUI as sg

layout = [
    [sg.Text('Введите Ваше имя:'), sg.InputText()],
    [sg.Text('Введите Ваш возраст:'), sg.Spin([i for i in range(1, 101)], initial_value=18)],
    [sg.Text('Выберите ваш любимый цвет:'), sg.Combo(['Красный', 'Зеленый', 'Синий'], default_value='Зеленый')],
    [sg.Checkbox('Подтверждаю данные', default=True)],
    [sg.Button('Ok'), sg.Button('Cancel')]
]
window = sg.Window('Пример макета PySimpleGUI', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'Ok':
        sg.popup(f"Привет, {values[0]}! Твой возраст: {values[1]}, любимый цвет: {values[2]}", title='Информация')
window.close()'''

'''import PySimpleGUI as sg
import os

def program():
    layout = [[sg.Text('Выберите файл:'), sg.Input(), sg.FileBrowse()],
            [sg.Button('Открыть'), sg.Button('Отмена')]]

    window = sg.Window('Файловый диалог', layout)

    while True:
        event, values = window.read()
        print(event, values)
        if event in (None, 'Отмена'):
            break
        elif event == 'Открыть':
            file_path = values[0]
            os.startfile(file_path)

    window.close()'''

'''def program():
    layout = [[sg.Text('Сохранить файл как:'), sg.Input(), sg.FileSaveAs()],
              [sg.Button('Сохранить'), sg.Button('Отмена')]]

    window = sg.Window('Диалог сохранения файла', layout)

    while True:
        event, values = window.read()

        if event in (None, 'Отмена'):
            break
        elif event == 'Сохранить':
            file_path = values[0]
            os.path.join(file_path)

    window.close()'''

import PySimpleGUI as sg
import os
import file_change
from viewer import show, delete


def spin(window):
    layout = [
        [sg.Text("Введите степень сжатия изображения(-ий):")],
        [sg.Spin(values=[x for x in range(1, 96)], readonly=True, key='-SPIN-')],
        [sg.Button('OK', size=(8, 1), key='-OK-')]

    ]
    new_window = sg.Window("Image Koef", layout)

    while True:
        event, values = new_window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == "-OK-":
            window["-SHOW-"].update(
                show(window["-NEW LIST-"].get_list_values(), window["-SHOW-"].get().split('\n')[0],
                     new_window["-SPIN-"].get()))
        new_window.close()


def office():
    file_list_column = [
        [sg.Text("File Change"), sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
         sg.FolderBrowse()],
        [sg.Listbox(values=[], enable_events=True, size=(40, 20), key="-FILE LIST-")],
    ]
    image_viewer_column = [
        [sg.Text("Доступные команды к файлам:")],
        [sg.Text(size=(40, 5), key="-SHOW-")],
        [sg.Listbox(values=[], enable_events=True, size=(40, 10), key="-NEW LIST-")],
        [sg.Button('Действие', size=(8, 1), disabled=True, key="-ENTER-")],
        [sg.Button('Удалить', size=(8, 1), disabled=True, button_color='red', key='-DELETE-')],
        [sg.Button('Убрать', size=(8, 1), disabled=True, key='-CLEAR-')],
        [sg.Button('Убрать все', size=(8, 1), disabled=True, key='-CLEAR ALL-')]
    ]
    layout = [[sg.Column(file_list_column), sg.VSeperator(), sg.Column(image_viewer_column), ]]
    window = sg.Window("Image Viewer", layout)

    new_list = []
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "-FOLDER-":
            folder = values["-FOLDER-"]
            file_change.change_catalog(folder)
            try:
                file_list = os.listdir(folder)
            except:
                file_list = []
            fnames = [f for f in file_list if os.path.isfile(os.path.join(folder, f))]
            window["-FILE LIST-"].update(fnames)
        '''try:
            window["-SHOW-"].update(show(values["-FILE LIST-"]))
        except:
            pass'''
        '''if len(window["-SHOW-"].get().split('\n')) == 2:
            window["-ENTER-"].update(disabled=False)
        else:
            window["-ENTER-"].update(disabled=True)
            #window["-SHOW-"].update(show_method(values["-FILE LIST-"]))
        #print(window["-SHOW-"].get().split('\n'))
        if len(window["-SHOW-"].get().split('\n')) > 0 and window["-SHOW-"].get().split('\n')[0] != '':
            window["-DELETE-"].update(disabled=False)
        else:
            window["-DELETE-"].update(disabled=True)'''
        if event == "-FILE LIST-":
            if values["-FILE LIST-"][0] not in new_list:
                new_list.append(values["-FILE LIST-"][0])
            window["-NEW LIST-"].update(new_list)
            window["-SHOW-"].update('\n'.join(show(new_list)))
            window["-CLEAR ALL-"].update(disabled=False)
            if len(window["-SHOW-"].get().split('\n')) == 2:
                window["-ENTER-"].update(disabled=False)
            else:
                window["-ENTER-"].update(disabled=True)
            if len(window["-SHOW-"].get().split('\n')) > 0 and window["-SHOW-"].get().split('\n')[0] != '':
                window["-DELETE-"].update(disabled=False)
            else:
                window["-DELETE-"].update(disabled=True)

        elif event == "-ENTER-":
            if 'сжатие' in window["-SHOW-"].get().split('\n')[0]:
                spin(window)
            else:
                window["-SHOW-"].update(
                    show(window["-NEW LIST-"].get_list_values(), folder + '/' + window["-SHOW-"].get().split("\n")[0]))
            window["-NEW LIST-"].update('')
            new_list.clear()
            window["-SHOW-"].update('\n'.join(show(new_list)))
            window["-ENTER-"].update(disabled=True)
            window["-DELETE-"].update(disabled=True)
            window["-CLEAR-"].update(disabled=True)
            window["-CLEAR ALL-"].update(disabled=True)

            folder = values["-FOLDER-"]
            file_change.change_catalog(folder)
            try:
                file_list = os.listdir(folder)
            except:
                file_list = []
            fnames = [f for f in file_list if os.path.isfile(os.path.join(folder, f))]
            window["-FILE LIST-"].update(fnames)

        elif event == "-DELETE-":
            window["-SHOW-"].update('')
            new_list.clear()
            delete(window["-NEW LIST-"].get_list_values())
            window["-NEW LIST-"].update('')
            window["-ENTER-"].update(disabled=True)
            window["-DELETE-"].update(disabled=True)
            window["-CLEAR-"].update(disabled=True)
            window["-CLEAR ALL-"].update(disabled=True)

            folder = values["-FOLDER-"]
            file_change.change_catalog(folder)
            try:
                file_list = os.listdir(folder)
            except:
                file_list = []
            fnames = [f for f in file_list if os.path.isfile(os.path.join(folder, f))]
            window["-FILE LIST-"].update(fnames)

        elif event == "-NEW LIST-":
            window["-CLEAR-"].update(disabled=False)

        elif event == "-CLEAR-":
            new_list.remove(values["-NEW LIST-"][0])
            window["-NEW LIST-"].update(new_list)
            window["-SHOW-"].update('\n'.join(show(new_list)))
            window["-CLEAR-"].update(disabled=True)
            if len(window["-NEW LIST-"].get_list_values()) == 0:
                window["-CLEAR ALL-"].update(disabled=True)
            if len(window["-SHOW-"].get().split('\n')) == 2:
                window["-ENTER-"].update(disabled=False)
            else:
                window["-ENTER-"].update(disabled=True)
            if len(window["-SHOW-"].get().split('\n')) > 0 and window["-SHOW-"].get().split('\n')[0] != '':
                window["-DELETE-"].update(disabled=False)
            else:
                window["-DELETE-"].update(disabled=True)

        elif event == "-CLEAR ALL-":
            window["-NEW LIST-"].update('')
            new_list.clear()
            window["-SHOW-"].update('\n'.join(show(new_list)))
            window["-CLEAR-"].update(disabled=True)
            window["-CLEAR ALL-"].update(disabled=True)
            window["-ENTER-"].update(disabled=True)
            window["-DELETE-"].update(disabled=True)

        if len(window["-NEW LIST-"].get_list_values()) > 0:
            pass
    window.close()