import PySimpleGUI as sg
import sqlite3
from functions import *
#jebac
# database
db = sqlite3.connect("LIFTMATE_DATABASE.db")
cursor = db.cursor()

window = create_window("account_info")

while True:
    event, values = window.read()

window.close()