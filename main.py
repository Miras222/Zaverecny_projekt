#!/usr/bin/env python3

from osoba import Osoba


osoby = [] #seznam pojištěných osob
pokracuj = True
while pokracuj:
    print("-----------------------------")
    print("Evidence pojistenych")
    print("-----------------------------\n")
    print("Vyberte si akci:")
    print("1 - Přidat nového pojištěného")
    print("2 - Vypsat všechny pojištěné")
    print("3 - Vyhledat pojištěného")
    print("4 - Konec")
    volba = int(input())
    if volba == 1:
        """
        Tato akce uživateli uožňuje zadat údaje
        nové pojištěné osoby a přidá ji do seznamu.
        """
        jmeno = input("Zadejte jméno pojištěného:\n")
        prijmeni = input("Zadejte příjmení:\n")
        vek = int(input("Zadejte věk:\n"))
        tel = int(input("Zadejte telefonní číslo:\n"))
        osoby.append(Osoba(jmeno, prijmeni, vek, tel)) #přidání osoby do seznamu pojištěných
        input("\nData byla uložena. Pokračujte libovolnou klávesou...")
    elif volba == 2:
        """
        Vypíše celý seznam pojištěných osob
        """
        for i in osoby:
            print(i)
        input("\nPokračujte libovolnou klávesou...")
    elif volba == 3:
        """
        Uživatel může pomocí zadání jména a příjmení
        vyhledat specifickou pojištěnou osobu v seznamu
        """
        hledane_jmeno = input("Zadejte jméno pojištěného:\n")
        hledane_prijmeni = input("Zadejte příjmení:\n")
        index = 0
        while len(osoby) > index:
            if hledane_jmeno.lower() == osoby[index].jmeno.lower() and hledane_prijmeni.lower() == osoby[index].prijmeni.lower():
                print(osoby[index])
            index += 1
        input("\nPokračujte libovolnou klávesou...")
    elif volba == 4:
        pokracuj = False
    else:
        print("Neplatná volba. Zadej číslo od 1 do 4!")

input("\n\nPro ukončení stiskni libovolnou klávesu...")

