#!/usr/bin/env python3

class Osoba:
    """
    Třída reprezentuje osoby, které jsou v evidenci pojištěných.
    """

    
    
    def __init__(self, jmeno, prijmeni, vek, tel):
        #Konstruktor
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.tel = tel

        
    
    def __str__(self):
        #Vypíše textovou reprezentaci pojištěné osoby
        return str(f"{self.jmeno}\t{self.prijmeni}\t{self.vek}\t{self.tel}")
