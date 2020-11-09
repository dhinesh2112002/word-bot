import PySimpleGUI as sg
from utils import get_meaning,get_synonyms,get_antonyms,get_example
sg.theme('dark green 1')
greeting = "Hi.Iam Chitti The Rebot.\n"
layout = [
    [sg.Multiline(greeting, font=("arial", 14), size=(70, 15), key='output')],
    [sg.InputText("", font=("Arial", 14), size=(50, 1), key='input', enable_events=True)],
    [sg.Button("Meaning", font=("Arial", 14), bind_return_key=True, key="meaning"),
     sg.Button("Synonyms", font=("Arial", 14), key='synonyms'),
     sg.Button("example", font=("Arial", 14), key='example'),
     sg.Button("Antonyms", font=("Arial", 14), key='antonyms'),
     sg.Button("Clear", font=("Arial", 14), key='clear')
    ]
]
def display_meaning(word):
    meaning=get_meaning(word)
    window['output'].print("Word: " + word)
    if meaning:
        window['output'].print("Meaning: ", meaning)
    else:
        display_error("Meaning Not Found")
def display_example(word):
    example=get_example(word)
    window['output'].print("Word: " + word)
    if example:
        window['output'].print("Example: ", example)
    else:
        display_error("Meaning Not Found")
def display_synonyms(word):
    synonyms=get_synonyms(word)
    window['output'].print("Word : " + word)
    if synonyms:
        window['output'].print("Synonyms: ", synonyms)
    else:
        display_error("No Synonyms Found")
def display_antonyms(word):
    antonyms=get_antonyms(word)
    window['output'].print("Word : " + word)
    if antonyms:
        window['output'].print("Antonyms: ", antonyms)
    else:
        display_error("No Antonyms Found")
def display_error(message):
    window['output'].print("Error : " +message, text_color='red')
if __name__=='__main__':
    window = sg.Window('File Explorer', layout)
    while True:
        event,values=window.Read()
        if event=='meaning':
            display_meaning(values['input'])
        elif event=='synonyms':
            display_synonyms(values['input'])
        elif event=='example':
            display_example(values['input'])
        elif event=='antonyms':
            display_antonyms(values['input'])
        elif event=='clear':
            window.FindElement('output').Update(greeting)
        elif event == sg.WINDOW_CLOSED:
            break
    window.close()
