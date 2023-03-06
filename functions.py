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



