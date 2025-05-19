import tkinter as tk
from tkinter import messagebox
import json

ADRESY = 'adresy.json'


class KsiazkaTelefoniczna:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Ksiazka telefonicza')
        self.root.geometry('400x500')
        self.numery = []
        
    
    def build_gui(self):
        # Imie
        tk.Label(self.root, text='Imie').pack(pady=5)
        self.imie = tk.Entry(self.root)
        self.imie.pack(pady=5)

        # Nazwisko
        tk.Label(self.root, text='Nazwisko').pack(pady=5)
        self.nazwisko = tk.Entry(self.root)
        self.nazwisko.pack(pady=5)

        # Nr telefonu
        tk.Label(self.root, text='Telefon').pack(pady=5)
        self.nr_tel = tk.Entry(self.root)
        self.nr_tel.pack(pady=5)

        # Przycisk dodawania
        btn_dodawania = tk.Button(self.root, text='Dodaj numer', command=self.add_entry)
        btn_dodawania.pack(pady=5)

        # Pole z numerami
        self.kontakty = tk.Listbox(self.root, width=50)
        self.kontakty.pack(pady=5)

        # Przycisk usuwania 
        btn_usuwania = tk.Button(self.root, text='Usun kontakt', command=self.delete_contact)
        btn_usuwania.pack(pady=5)

    def add_entry(self):
        imie = self.imie.get()
        nazwisko = self.nazwisko.get()
        nr_tel = self.nr_tel.get()

        if imie and nazwisko and nr_tel:
            kontakt = f'{imie} {nazwisko} | {nr_tel}'
            self.numery.append(kontakt)
            self.kontakty.insert(tk.END, kontakt)
            self.clear_fields()
            messagebox.showinfo('Informacja', 'Dodano kontakt')
    
    def delete_contact(self):
        selected = self.kontakty.curselection()
        if selected:
            index = selected[0]
            self.kontakty.delete(index)
            del self.numery[index]
        else:
            messagebox.showinfo('Informacja', 'Wybierz kontakt do usuniecia')
    
    def clear_fields(self):
        self.imie.delete(0, tk.END)
        self.nazwisko.delete(0, tk.END)
        self.nr_tel.delete(0, tk.END)
    
    def run(self):
        self.build_gui()
        self.root.mainloop()

if __name__ == '__main__':
    app = KsiazkaTelefoniczna()
    app.run()