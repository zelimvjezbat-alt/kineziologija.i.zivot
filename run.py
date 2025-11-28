import webbrowser
import os

# Dohvati put do trenutne mape gdje je run.py
folder_path = os.path.dirname(__file__)

# Put do landing.html
html_file = os.path.join(folder_path, 'landing.html')

# Provjera da datoteka postoji
if os.path.exists(html_file):
    # Otvori landing.html u default browseru
    webbrowser.open_new_tab(f'file://{html_file}')
    print("Otvara se landing.html u browseru...")
else:
    print("Datoteka landing.html nije pronađena!")
