class Pojisteny:
    def __init__(self, jmeno, prijmeni, vek, telefon, typ_pojisteni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon
        self.typ_pojisteni = typ_pojisteni
    def __str__(self):
        return f"{self.jmeno},{self.prijmeni}, věk:{self.vek}, " \
               f"tel.číslo:{self.telefon}, typ pojištění: {self.typ_pojisteni}."

prvni = Pojisteny("Josef", "První", 60, 222333444, "cestovní")
druhy = Pojisteny("Libuše", "Druhá", 40, 222555777, "cestovní")
treti = Pojisteny("Václav", "Třetí", 10, 222666888, "cestovní")



