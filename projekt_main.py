from projekt_evidence_pojistenych import Evidence
evidence = Evidence()
print("Toto je konzolová evidence pojištěných!")
pokracovat ="ano"
while(pokracovat =="ano"):
    akce = int(input("Chcete-li přidat nového pojištěnce, stiskněte 1, \n"
                 "chcete-li zobrazit seznam pojištěných, stiskněte 2 \n "
                 "chcete-li vyhledat pojištěnce, stiskněte 3 \n"
                 "chcete-li ukončit program, stiskněte 4 \n"))
    if (akce == 1):
        evidence.pridat_pojistence()
    elif (akce == 2):
        evidence.zobraz_evidenci()
    elif (akce == 3):
        evidence.vypis_pojistence()
    elif (akce == 4):
        print("Konec programu.")
    else:
        print("Neplatná volba!")
    pokracovat = input("Přejete si pokračovat? ano / ne : ")
print("Konec programu.")





