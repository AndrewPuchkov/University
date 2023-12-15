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
from file_change import *
from viewer import show, delete, files_with_str1, files_with_start1, files_with_end1, files_with_expansion1


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


def gms_window():
    layout = [
        [sg.Text("Удаление по подстроке: ", expand_y=True, expand_x=True),
         sg.InputText(key='--INPUT DELETE STR--', enable_events=True)],
        [sg.Button('Удалить', size=(8, 1), key='--DELETE STR--', button_color='red')],
        [sg.Text("Удаление по началу названия: ", expand_y=True, expand_x=True),
         sg.InputText(key='--INPUT DELETE START STR--', enable_events=True)],
        [sg.Button('Удалить', size=(8, 1), key='--DELETE START STR--', button_color='red')],
        [sg.Text("Удалению по концу названия: ", expand_y=True, expand_x=True),
         sg.InputText(key='--INPUT DELETE END STR--', enable_events=True)],
        [sg.Button('Удалить', size=(8, 1), key='--DELETE END STR--', button_color='red')],
        [sg.Text("Удаление по расширению: ", expand_y=True, expand_x=True),
         sg.InputText(key='--INPUT DELETE EXP--', enable_events=True)],
        [sg.Button('Удалить', size=(8, 1), key='--DELETE EXP--', button_color='red')],
    ]
    # Возвращаем окно с названием "GMS to Deg", содержащее описанный выше интерфейс
    return sg.Window('GMS to Deg', layout, size=(500, 500), resizable=True, finalize=True)


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
        [sg.Button('Удаление файлов', size=(8, 1), disabled=False, button_color='red', key='-DELETE-')],
        [sg.Button('Убрать', size=(8, 1), disabled=True, key='-CLEAR-')],
        [sg.Button('Убрать все', size=(8, 1), disabled=True, key='-CLEAR ALL-')]
    ]
    '''delete_viewer_column = [

        [sg.Text("Доступно удаление по:")],
        [sg.Text(size=(40, 5), key="-SHOW DELETE-")],

    ]'''
    layout = [[sg.Column(file_list_column), sg.VSeperator(), sg.Column(image_viewer_column), ]]
    # layout1 = [[sg.Column()]]
    window = sg.Window("Image Viewer", layout)
    # window_for_delete = sg.Window("Удаление файлов", layout1)
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
            window_delete = gms_window()
            flag_delete = True
            while flag_delete:
                window1, event1, values1 = sg.read_all_windows()
                if window1 == window_delete:
                    if event1 == '--INPUT DELETE STR--':
                        delete_str = window1['--INPUT DELETE STR--'].get()
                        print(delete_str)
                    elif event1 == sg.WINDOW_CLOSED:
                        window1.close()
                        flag_delete = False
                    elif event1 == '--INPUT DELETE START STR--':
                        delete_start_str = window1['--INPUT DELETE START STR--'].get()
                    elif event1 == '--INPUT DELETE END STR--':
                        delete_end_str = window1['--INPUT DELETE END STR--'].get()
                    elif event1 == '--INPUT DELETE EXP--':
                        delete_exp = window1['--INPUT DELETE EXP--'].get()
                    elif event1 == '--DELETE STR--':
                        fws1 = files_with_str1(delete_str, file_list)
                        for i in fws1:
                            os.remove(i)
                        # print(files_with_str1(delete_str, file_list))
                    elif event1 == '--DELETE START STR--':
                        fwstart1 = files_with_start1(delete_start_str, file_list)
                        for i in fwstart1:
                            os.remove(i)
                        # print(files_with_start1(delete_start_str, file_list))
                    elif event1 == '--DELETE END STR--':
                        fwe1 = files_with_end1(delete_end_str, file_list)
                        for i in fwe1:
                            os.remove(i)
                        # print(files_with_end1(delete_end_str, file_list))
                    elif event1 == '--DELETE EXP--':
                        fwexp1 = files_with_expansion1(delete_exp, file_list)
                        for i in fwexp1:
                            os.remove(i)

                        # print(files_with_expansion1(delete_exp, file_list))

            '''window["-SHOW-"].update('')
            new_list.clear()
            delete(window["-NEW LIST-"].get_list_values())
            window["-NEW LIST-"].update('')
            window["-ENTER-"].update(disabled=True)
            window["-DELETE-"].update(disabled=True)
            window["-CLEAR-"].update(disabled=True)
            window["-CLEAR ALL-"].update(disabled=True)
            folder = values["-FOLDER-"]
            file_change.change_catalog(folder)'''
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
