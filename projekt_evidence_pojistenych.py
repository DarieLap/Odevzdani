from projekt_pojisteny import Pojisteny
class Evidence:
    def __init__(self):
        self.evidence_pojistenych = []
    def pridat_pojistence(self):
        jmeno = input("Zadejte jméno pojištěnce: ")
        prijmeni = input("Zadejte příjmení pojištěnce: ")
        vek = input("Zadejte věk pojištěnce: ")
        telefon = input("Zadejte telefonní číslo pojištěnce: ")
        typ_pojisteni = input("Zadejte typ uzavřeného pojištění: ")
        novy_pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon, typ_pojisteni)
        self.evidence_pojistenych.append(novy_pojisteny)
        print(f"Přidali jste nového pojištěnce {novy_pojisteny}.")
    def zobraz_evidenci(self):
        for pojisteny in self.evidence_pojistenych:
            print(pojisteny)
    def vypis_pojistence(self):
        zadane_jmeno = input("Zadejte jméno pojištěnce: ")
        zadane_prijmeni = input("Zadejte příjmení pojištěnce: ")
        for pojisteny in self.evidence_pojistenych:
            if zadane_jmeno == pojisteny.jmeno and zadane_prijmeni == pojisteny.prijmeni:
                print(pojisteny)







