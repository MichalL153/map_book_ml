from tkinter import *
import requests
import tkintermapview
from bs4 import BeautifulSoup

users = []
employee = []


class User:
    def __init__(self, name, surname, location):
        self.name: str = name
        self.surname: str = surname
        self.location: str = location
        self.coords: list = User.get_coordinates(self)

        self.marker = map_widget.set_marker(
            self.coords[0],
            self.coords[1],
            text=f"{self.name}"
        )

    def get_coordinates(self) -> list:
        url: str = f'https://pl.wikipedia.org/wiki/{self.location}'
        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')
        return [
            float(response_html.select('.latitude')[1].text.replace(",", ".")),
            float(response_html.select('.longitude')[1].text.replace(",", "."))
        ]


def show_users() -> None:
    listbox_lista_klientow.delete(0, END)
    for idx, user in enumerate(users):
        listbox_lista_klientow.insert(idx, f'{user.name} {user.surname} {user.location}')


def add_user() -> None:
    name = entry_imie.get()
    surname = entry_nazwisko.get()
    location = entry_lokalizacja.get()
    users.append(User(name, surname, location))

    show_users()

    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_lokalizacja.delete(0, END)

    entry_imie.focus()

def remove_user() -> None:
    i = listbox_lista_klientow.index(ACTIVE)
    users[i].marker.delete()
    users.pop(i)
    show_users()


def show_user_details() -> None:
    i = listbox_lista_klientow.index(ACTIVE)
    imie = users[i].name
    label_imie_szczegoly_obiektu_wartosc.config(text=imie)
    nazwisko = users[i].surname
    label_nazwisko_szczegoly_obiektu_wartosc.config(text=nazwisko)
    lokalizacja = users[i].location
    label_lokalizacja_szczegoly_obiektu_wartosc.config(text=lokalizacja)
    map_widget.set_position(users[i].wspolrzedne[0], users[i].wspolrzedne[1])
    map_widget.set_zoom(12)


def edit_user_data() -> None:
    i = listbox_lista_klientow.index(ACTIVE)
    entry_imie.insert(0, users[i].name)
    entry_nazwisko.insert(0, users[i].surname)
    entry_lokalizacja.insert(0, users[i].location)
    button_dodaj_uzytkownika.config(text="Zapisz zmiany", command=lambda: update_user(i))


def update_user(i) -> None:
    users[i].name = entry_imie.get()
    users[i].surname = entry_nazwisko.get()
    users[i].location = entry_lokalizacja.get()
    users[i].wspolrzedne = User.get_coordinates(users[i])
    users[i].marker.delete()
    users[i].marker = map_widget.set_marker(users[i].wspolrzedne[0], users[i].wspolrzedne[1],
                                            text=f"{users[i].name}")
    show_users()
    button_dodaj_uzytkownika.config(text="Dodaj użytkownika", command=add_user)
    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_lokalizacja.delete(0, END)
    entry_imie.focus()


def show_employee() -> None:
    listbox_lista_pracownikow.delete(0, END)
    for idx, user in enumerate(employee):
        listbox_lista_pracownikow.insert(idx, f'{user.name} {user.surname} {user.location}')


def add_user_employee() -> None:
    name = entry_imie.get()
    surname = entry_nazwisko.get()
    location = entry_lokalizacja.get()
    employee.append(User(name, surname, location))
    show_employee()
    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_lokalizacja.delete(0, END)
    entry_imie.focus()


def remove_user_employee() -> None:
    i = listbox_lista_pracownikow.index(ACTIVE)
    employee[i].marker.delete()
    employee.pop(i)
    show_employee()


def show_user_details_employee() -> None:
    i = listbox_lista_pracownikow.index(ACTIVE)
    imie = employee[i].name
    label_imie_szczegoly_obiektu_wartosc.config(text=imie)
    nazwisko = employee[i].surname
    label_nazwisko_szczegoly_obiektu_wartosc.config(text=nazwisko)
    lokalizacja = employee[i].location
    label_lokalizacja_szczegoly_obiektu_wartosc.config(text=lokalizacja)
    map_widget.set_position(employee[i].wspolrzedne[0], employee[i].wspolrzedne[1])
    map_widget.set_zoom(12)


def edit_user_data_employee() -> None:
    i = listbox_lista_pracownikow.index(ACTIVE)
    entry_imie.insert(0, employee[i].name)
    entry_nazwisko.insert(0, employee[i].surname)
    entry_lokalizacja.insert(0, employee[i].location)
    button_dodaj_uzytkownika.config(text="Zapisz zmiany", command=lambda: update_user(i))


def update_user_employee(i) -> None:
    employee[i].name = entry_imie.get()
    employee[i].surname = entry_nazwisko.get()
    employee[i].location = entry_lokalizacja.get()
    employee[i].wspolrzedne = User.get_coordinates(employee[i])
    employee[i].marker.delete()
    employee[i].marker = map_widget.set_marker(employee[i].wspolrzedne[0], employee[i].wspolrzedne[1],
                                               text=f"{employee[i].name}")
    show_employee()
    button_dodaj_uzytkownika.config(text="Dodaj użytkownika", command=add_user)
    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_lokalizacja.delete(0, END)
    entry_imie.focus()


def login():
    poprawnylogin = "xdd"
    poprawnehaslo = "xd"
    login = entry_login.get()
    haslo = entry_haslo.get()
    if poprawnylogin == login and poprawnehaslo == haslo:
        pokazmenu()


def pokazmenu():
    rama.destroy()
    glownemenu.pack(fill="both", expand=True)


root = Tk()
root.title("Portal randkowy")
root.geometry("1024x760")

rama = Frame(root)
rama.pack(pady=20)

label_login = Label(rama, text="Login")
label_login.grid(row=0, column=0, pady=5)
entry_login = Entry(rama)
entry_login.grid(row=0, column=1, pady=5)

label_haslo = Label(rama, text="Haslo")
label_haslo.grid(row=1, column=0, pady=5)
entry_haslo = Entry(rama, show='*')
entry_haslo.grid(row=1, column=1, pady=5)

przycisklogin = Button(rama, text="Zaloguj", command=login)
przycisklogin.grid(row=2, columnspan=2, pady=10)

glownemenu = Frame(root)

ramka_lista_klientow = Frame(glownemenu)
ramka_lista_pracownicy = Frame(glownemenu)
ramka_formularz = Frame(glownemenu)
ramka_szczegoly_obiektu = Frame(glownemenu)

ramka_lista_klientow.grid(column=0, row=0, padx=50)
ramka_lista_pracownicy.grid(column=1, row=0, padx=50)
ramka_formularz.grid(column=2, row=0)
ramka_szczegoly_obiektu.grid(column=0, row=1, columnspan=3, padx=50, pady=20)

label_lista_klientow = Label(ramka_lista_klientow, text="Lista klientów: ")
listbox_lista_klientow = Listbox(ramka_lista_klientow, width=50)
button_pokaz_szczegoly = Button(ramka_lista_klientow, text="Pokaż szczegóły", command=show_user_details)
button_usun_obiekkt = Button(ramka_lista_klientow, text="Usuń obiekt", command=remove_user)
button_edytuj_obiekt = Button(ramka_lista_klientow, text="Edytuj obiekt", command=edit_user_data)

label_lista_klientow.grid(row=0, column=0, columnspan=3)
listbox_lista_klientow.grid(row=1, column=0, columnspan=3)
button_pokaz_szczegoly.grid(row=2, column=0)
button_usun_obiekkt.grid(row=2, column=1)
button_edytuj_obiekt.grid(row=2, column=2)

label_lista_pracownikow = Label(ramka_lista_pracownicy, text="Lista pracowników: ")
listbox_lista_pracownikow = Listbox(ramka_lista_pracownicy, width=50)
button_pokaz_szczegoly_prac = Button(ramka_lista_pracownicy, text="Pokaż szczegóły", command=show_user_details_employee)
button_usun_obiekkt_prac = Button(ramka_lista_pracownicy, text="Usuń obiekt", command=remove_user_employee)
button_edytuj_obiekt_prac = Button(ramka_lista_pracownicy, text="Edytuj obiekt", command=edit_user_data_employee)

label_lista_pracownikow.grid(row=0, column=0, columnspan=3)
listbox_lista_pracownikow.grid(row=1, column=0, columnspan=3)
button_pokaz_szczegoly_prac.grid(row=2, column=0)
button_usun_obiekkt_prac.grid(row=2, column=1)
button_edytuj_obiekt_prac.grid(row=2, column=2)
# formularz

label_formularz = Label(ramka_formularz, text="Formularz: ")
label_imie = Label(ramka_formularz, text="Imię: ")
label_nazwisko = Label(ramka_formularz, text="Nazwisko: ")
label_lokalizacja = Label(ramka_formularz, text="Lokalizacja: ")

entry_imie = Entry(ramka_formularz)
entry_nazwisko = Entry(ramka_formularz)
entry_lokalizacja = Entry(ramka_formularz)

label_formularz.grid(row=0, column=0, columnspan=2)
label_imie.grid(row=1, column=0, sticky=W)
label_nazwisko.grid(row=2, column=0, sticky=W)
label_lokalizacja.grid(row=4, column=0, sticky=W)

entry_imie.grid(row=1, column=1)
entry_nazwisko.grid(row=2, column=1)
entry_lokalizacja.grid(row=4, column=1)

button_dodaj_uzytkownika = Button(ramka_formularz, text="Dodaj klienta", command=add_user)
button_dodaj_uzytkownika.grid(row=6, column=0)
button_dodaj_pracownika = Button(ramka_formularz, text="Dodaj pracownika", command=add_user_employee)
button_dodaj_pracownika.grid(row=6, column=1)

# szczegóły obiektu

label_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Szczegóły użytkownika:")
label_imie_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Imię: ")
label_nazwisko_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Nazwisko: ")
label_lokalizacja_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Lokalizacja: ")

label_imie_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...", width=10)
label_nazwisko_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...", width=10)
label_lokalizacja_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...", width=10)

label_szczegoly_obiektu.grid(row=0, column=0, sticky=W)
label_imie_szczegoly_obiektu.grid(row=1, column=0, sticky=W)
label_imie_szczegoly_obiektu_wartosc.grid(row=1, column=1)
label_nazwisko_szczegoly_obiektu.grid(row=1, column=2)
label_nazwisko_szczegoly_obiektu_wartosc.grid(row=1, column=3)
label_lokalizacja_szczegoly_obiektu.grid(row=1, column=6)
label_lokalizacja_szczegoly_obiektu_wartosc.grid(row=1, column=7)

# map widget
map_widget = tkintermapview.TkinterMapView(ramka_szczegoly_obiektu, width=900, height=400)
map_widget.set_position(52.2, 21.0)
map_widget.set_zoom(6)
map_widget.grid(row=2, column=0, columnspan=8)

root.mainloop()