import PySimpleGUI as sg
import pandas as pd

sg.theme('DarkGreen4')

EXCEL_FILE = r'data.xlsx'

df = pd.read_excel(EXCEL_FILE)

layout = [
    [sg.Text('Input your data : ')],
    [sg.Text('Nama', size=(15, 1)), sg.InputText(key='Nama')],
    [sg.Text('No Telp', size=(15, 1)), sg.InputText(key='Tlp')],
    [sg.Text('Alamat', size=(15, 1)), sg.Multiline(key='Alamat')],
    [sg.Text('Tgl Lahir', size=(15, 1)), sg.InputText(key='Tgl Lahir'),
     sg.CalendarButton('Kalender', target='Tgl Lahir', format=('%d-%M-%Y'))],
    [sg.Text('Jenis Kelamin', size=(15, 1)), sg.Combo(['pria', 'wanita'], key='Jenis Kelamin')],
    [sg.Text('Hobi', size=(15, 1)), sg.Checkbox('Sepak Bola', key='Sport'),
     sg.Checkbox('Menonton', key='Menonton'),
     sg.Checkbox('Musik', key='Musik'),
     sg.Checkbox('Programming', key='Programmer')],
    [sg.Submit(), sg.Button('clear'), sg.Exit()]
]

window = sg.Window('Form pendaftaran', layout)

def clear_input():
    for key in values:
        window[key]('')
    return None

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'EXIT':
        break
    if event == 'Clear':
        clear_input()
    if event == 'Submit':
        df = pd.concat([df, pd.DataFrame(values, index=[0])], ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        sg.popup('Data Success')
        clear_input()
window.close()
