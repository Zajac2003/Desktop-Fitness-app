import PySimpleGUI as sg

#jebac zydow
def create_window(zakladka):
    # Definiujemy układ graficzny okna, zależne od 'zakladka'
    if zakladka == 'menu':
        sg.theme('DarkAmber')
        layout = [
                    [sg.Text("TU BEDZIE EXP", key='EXP'), sg.MenuBar([["=",["Opcja1", "Opcja2"]]])],
                    [sg.Text("TU BEDZIE EXP", key='EXP')],
                    [sg.Button("OK")]
                  ]

        window = sg.Window("Okno PySimpleGUI", layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == 'OK':
                break

        window.close()
    #zakladka, ktora pojawia sie, gdy klikniemy "dodaj post"
    elif zakladka == "post_add":
        pass
    # zakladka, ktora pojawia sie, gdy klikniemy "przegladaj"
    elif zakladka == "post_lookup":
        pass
    # zakladka, ktora pojawia sie, gdy klikniemy "wyszukaj ziomali"
    elif zakladka == "post_lookup":
        pass

    # zakladka, account_info do uzupelniania roznych informacji
    elif zakladka == "account_info":
        sg.theme('Dark blue')
        layout = [
                    [sg.Input(), sg.Text("Nickname")],
                    [sg.Input(), sg.Text("Team ID")],
                    [sg.Input(), sg.Text("Weight")],
                    [sg.Input(), sg.Text("Age")],
                    [sg.Input(), sg.Text("Gender")],
                    [sg.Input(), sg.Text("Height")],
                    [sg.Button("Save", key="SaveAccountInformation")]
                    
                  ]

        window = sg.Window("Okno PySimpleGUI", layout)
        while True:
            event, values = window.read()
            if event == "SaveAccountInformation":
                print("dziala hehe")
                print(values[0])
            if event == sg.WIN_CLOSED or event == 'OK':
                break

        window.close()


