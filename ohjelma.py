tankkikoko = 80 #Tämä on auton tankkikoko/kuinka paljon polttoainetta mahtuu. 
#Jos haluttu tankkausmäärä ylittää tämän arvon, ohjelma estää tankkauksen.

def bensahinnankeskiarvo():
    # Tämä aukaisee bensanhintojen tietokannan, laskee keskiarvon, ja palauttaa sen string muodossa.
    tallennettu_tieto = open("tietokanta.txt","r").read()
    lista_litra_hintoja = list(map(float, tallennettu_tieto.split("|")))
    keskiarvo = sum(lista_litra_hintoja) / len(lista_litra_hintoja)
    return str(keskiarvo)

def lisaahintojenkeskiarvoon(arvo):
    # Tämä lisää bensahinnan bensanhintojen tietokantaan.
    tallennettu_tieto = open("tietokanta.txt","r").read()
    tallennettu_tieto += "|" + str(arvo)
    open("tietokanta.txt","w").write(tallennettu_tieto)


while 1:
    print("\n\n-- Hinta Laskuri --")
    if(input("kirjoita aloita aloittaaksesi \n> ") == "aloita"):
        #Kun käyttäjä kirjoittaa aloita, aloitetaan ohjelma, kysytään ensin tietoa.
        polttoaine = input("Mitä polttoainetta tankkaat? Esim Diesel, Bensiini\n> ")
        maara = input("Kuinka paljon haluat tankata? (Litroina)\n> ")
        try:
            #Jos maara on validi, katsotaan mahtuuko se tankkiin. jos ei mahdu niin printataan tämä tieto.
            maara = float(maara)
            if maara < tankkikoko:
                litrahinta = input("Mikä on polttoaineen litrahinta?\n> ")
                try:
                    #Jos litrahinta on validi, lasketaan yhteishinta, ja printataan kaikki tieto käyttäjälle hienosti.
                    #Lisätään myös litrahinta hintojen tietokantaan, ja lasketaan uusi bensahintojen keskiarvo
                    #Näytetään keskiarvo käyttäjälle.

                    litrahinta = float(litrahinta)
                    print("Tämän tankkauksen ({}: {:.2f} litraa) hinta on euroina {:.2f}€".format(polttoaine, maara, maara*litrahinta))
                    lisaahintojenkeskiarvoon(litrahinta)
                    print("Ohjelman käyttäjien litrahintojen keskiarvo on nyt {:.2f}€/litra".format(float(bensahinnankeskiarvo())))
                except:
                    print("Litrahinta ei voi olla kirjain, kirjoita numero!")
            else:
                print("Tankkiisi ei mahdu niin paljoa polttoainetta. Vähennä polttoaineen määrää!")
        except:
            print("Kirjoita litramäärä numeroina, älä käytä kirjaimia!")



