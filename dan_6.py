# Datoteka ili File - imenovani prostor sa podacima
# Direktorijum ili Folder - imenovani prostor sa vise fajlova u sebi

# Modovi otvaranja fajla:
#   r - read - datoteka otvorena read-only (samo citanje)
#   w - write - datoteka otvorena za pisanje i citanje - brise se sav sadrzaj i kreira se novi
#   a - append - datoteka otvorena za piisanje i citanje - stari sadrzaj se zadrazava i kreira se novi
#   + - (ako bismo napisali r+) otvoreno za read, ali ako zapocnemo pisanje, bice dozvoljeno, prema drugom.
#   t/b - tekstualno ili binarno (default: t)

# dat = open("izlaz.txt", "w")
# dat.write("Neki tekst")
# dat.flush() # -> Save
# dat.close() # -> Close - obavezno zatvoriti

# broj_testova = int(input("Koliko testova cete uneti? "))

# if broj_testova < 1:
#     print("Broj testova mora biti veci od 0.")
#     exit()

# testovi = []

# for i in range(broj_testova):
#     indeks = input(f"Unesite indeks za {i + 1}. test: ")
#     predmet = input(f"Unesite predmet za {i + 1}. test: ")
#     bodovi = input(f"Unesite bodove za {i + 1}. test: ")

#     testovi.append({
#         "indeks": indeks,
#         "predmet": predmet,
#         "bodovi": bodovi
#     })

# # Obrada
# testovi.sort(key = lambda test : test['bodovi'])

# # Izlaz
# dat = open("testovi.dat", "w")

# for test in testovi:
#     dat.write(test['indeks'])
#     dat.write(test['predmet'])
#     dat.write(str(test['bodovi']))

#     dat.flush()
#     dat.close

# try:
#     dat = open("testovi.dat", "r")

#     testovi = []

#     while True:
#         prvi_red = dat.readline().strip()

#         if prvi_red == '':
#             break

#         drugi_red = dat.readline().strip()
#         treci_red = dat.readline().strip()

#         test = {
#             "indeks": prvi_red,
#             "predmet": drugi_red,
#             "bodovi": float(treci_red)
#         }

#         testovi.append(test)

#     print(testovi)
# except FileNotFoundError:
#     print("Nije moguce raditi sa fajlom koji ne postoji.")
# except IndexError:
#     print("Pokusavate da pristupite indeksu koji ne postoji.")

# Primer zadatka koji ce biti na ispitu:

try:
    roboti = []

    with open("roboti.txt", "r") as f:
        while True:
            id_broj = f.read(3)

            if id_broj == '':
                break

            model = f.read(6)
            proizvodjac = f.readline().strip()

            drugi_red = f.readline().strip()
            delovi_drugog_reda = drugi_red.split(' ')

            snaga = int(delovi_drugog_reda[0])
            bssk = int(delovi_drugog_reda[1])

            robot = {
                "id": int(id_broj),
                "model": model,
                "proizvodjac": proizvodjac,
                "snaga": snaga,
                "bssk": bssk
            }

            roboti.append(robot)

    print(roboti)

except:
    print("Neka greska se dogodila!")