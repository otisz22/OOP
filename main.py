from datetime import date
from szalloda import Szalloda
from szobak import EgyagyasSzoba, KetagyasSzoba


def main():
    szalloda = Szalloda("Pihenő Hotel")

    szoba1 = EgyagyasSzoba(szobaszam=101, ar=15000)
    szoba2 = KetagyasSzoba(szobaszam=201, ar=18000)
    szoba3 = KetagyasSzoba(szobaszam=202, ar=80000)

    szalloda.hozzaad_szoba(szoba1)
    szalloda.hozzaad_szoba(szoba2)
    szalloda.hozzaad_szoba(szoba3)

    szalloda.foglalas(szobaszam=101, datum=date(2023, 12, 25))
    szalloda.foglalas(szobaszam=201, datum=date(2023, 12, 26))
    szalloda.foglalas(szobaszam=202, datum=date(2023, 12, 27))
    szalloda.foglalas(szobaszam=101, datum=date(2023, 12, 28))
    szalloda.foglalas(szobaszam=201, datum=date(2023, 12, 29))

    print("Szálloda neve:", szalloda.nev)

    while True:
        print("\nVálasszon műveletet:")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("0. Kilépés")

        valasztas = input("Választás (0-3): ")

        if valasztas == "0":
            break
        elif valasztas == "1":
            print("Szobák:")
            for szoba in szalloda.szobak:
                print(f"Szoba száma: {szoba.szobaszam}, Ár: {szoba.ar}")
            try:
                szobaszam = int(input("Adja meg a szoba számát: "))

                while True:
                    datum_str = input("Adja meg a dátumot (ÉÉÉÉ-HH-NN): ")
                    try:
                        datum = date(*map(int, datum_str.split("-")))
                        break
                    except Exception:
                        print("Hiba: Érvénytelen dátum formátum. Próbálja újra.")

                ar = szalloda.foglalas(szobaszam, datum)
                if ar is not None:
                    print(f"Sikeres foglalás! Ár: {ar}")
                else:
                    print(
                        "Hiba a foglalás során. Ellenőrizze a szoba számát és a dátumot.")
            except Exception:
                print("Hiba: Érvénytelen bemenet. Szíveskedjen érvényes számot megadni.")

        elif valasztas == "2":
            try:
                print("\nFoglalások:")
                for index, foglalas in enumerate(szalloda.foglalasok):
                    print(index)
                foglalas_index = int(
                    input("\nAdja meg a lemondani kívánt foglalás sorszámát: "))
                if 0 <= foglalas_index < len(szalloda.foglalasok):
                    foglalas = szalloda.foglalasok[foglalas_index]
                    if szalloda.lemondas(foglalas):
                        print("Sikeres lemondás.")
                    else:
                        print("Hiba a lemondás során.")
                else:
                    print("Érvénytelen sorszám.")
            except Exception:
                print("Hiba: Érvénytelen bemenet. Szíveskedjen érvényes számot megadni.")

        elif valasztas == "3":
            print("Foglalások:")
            szalloda.listaz_foglalasok()

        else:
            print("Érvénytelen választás.")


if __name__ == "__main__":
    main()
