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
from viewer import show, show_method, Del


def office():
    file_list_column = [
        [sg.Text("Image Folder"), sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
         sg.FolderBrowse()],
        [sg.Listbox(values=[], enable_events=True, size=(40, 20), key="-FILE LIST-")],
    ]
    image_viewer_column = [
        [sg.Text("Доступные команды к файлам:")],
        [sg.Text(size=(40, 5), key="-SHOW-")],
        #[sg.Listbox(values=[], enable_events=True, size=(40, 10), key="-NEW LIST-")],
        [sg.Button('Действие', size=(8, 1), disabled=True, key="-ENTER-")],
        [sg.Button('Удалить', size=(8, 1), disabled=True, button_color='red', key='-DELETE-')],
    ]
    layout = [[sg.Column(file_list_column), sg.VSeperator(), sg.Column(image_viewer_column), ]]
    window = sg.Window("Image Viewer", layout)
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
        try:
            window["-SHOW-"].update(show())
        except:
            pass
        if event == "-FILE LIST-":
            #filenames = [values["-FILE LIST-"]]
            #window["-NEW LIST-"].update(' '.join(filenames))
            window["-ENTER-"].update(disabled=False)
            window["-SHOW-"].update(show_method(values["-FILE LIST-"]))
            window["-DELETE-"].update(disabled=False)
        elif event == "-ENTER-":
            window["-SHOW-"].update(show_method(values["-FILE LIST-"], flag=True))
            window["-ENTER-"].update(disabled=True)
            window["-DELETE-"].update(disabled=True)
        elif event == "-DELETE-":
            window["-SHOW-"].update(Del(values["-FILE LIST-"]))
            window["-ENTER-"].update(disabled=True)
            window["-DELETE-"].update(disabled=True)
    window.close()
