### Author: Łukasz Jaremek
### Date: 16.08.2020

def zwieksz_znak(znak, znaki):
    indeks = znaki.index(znak) + 1
    if indeks >= len(znaki):
        return "x"
    else:
        return znaki[indeks]


# Wejscie:
#   przedzial dlugosci generowanych wariacji
#   Znaki z których mają powstać wariacje
# Wynik:
#   generowane wariacje
def wariacje(dlugosci, znaki):
    znaki = list(map(str, znaki))
    
    dlugosc = dlugosci[0]
    dlugosc_max = dlugosci[1]

    pierwszy_znak = znaki[0]
    ostatni_znak = znaki[-1]
    
    wariacja = list(pierwszy_znak * dlugosc)
    
    istnieja_wariacje = True
    while istnieja_wariacje:
        # zwroc aktualną permutację
        yield "".join(wariacja)
        # sprawdz, czy ostatni znak wariacji == ostatni_znak:
        if wariacja[-1] != ostatni_znak:
        #   jeśli nie:
        #       zwiększ ostatni znak wariacji o jeden
            wariacja[-1] = zwieksz_znak(wariacja[-1], znaki)
        #   jeśli tak:
        else:
        #       ostatni znak permutacji = pierwszy_znak
            wariacja[-1] = pierwszy_znak
        #       for liczba in przedzial 2 do dlugosc:
            for liczba in range(2, dlugosc+1):
        #           liczba = -liczba
                liczba = -liczba
        #           czy wariacja[liczba] == ostatni_znak:
                if wariacja[liczba] != ostatni_znak:
        #               jeśli nie:
        #                   zwiększ wariacja[liczba] o jeden znak
                    wariacja[liczba] = zwieksz_znak(wariacja[liczba], znaki)
        #                   break
                    break
        #               jeśli tak:
                else:
        #                   spróbuj:
                    try:
        #                       ustaw wariacja[liczba] = pierwszy_znak
                        wariacja[liczba] = pierwszy_znak
        #                       jesli wariacja[liczba-1] != ostatni znak:
                        if wariacja[liczba-1] != ostatni_znak:
        #                           zwieksz wariacja[liczba-1] o jeden znak
                            wariacja[liczba-1] = zwieksz_znak(wariacja[liczba-1], znaki)
        #                           przerwij petle
                            break
        #                   jeśli IndexError:
                    except IndexError:
        #                       dlugosc += 1
                        dlugosc += 1
        #                       jeśli dlugosc > dlugosc_max:
                        if dlugosc > dlugosc_max:
        #                           zakoncz wszystko
                            istnieja_wariacje = False
                            break
        #                       jeśli nie:
                        else:
        #                           wariacja = [znak[0] * dlugosc]
                            wariacja = list(pierwszy_znak[0] * dlugosc)

znaki = list("0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")

        # while istnieja_wariacje:
        # zwroc aktualną wariację
        # sprawdz, czy ostatni znak wariacji == ostatni_znak:
        #   jeśli nie:
        #       zwiększ ostatni znak wariacji o jeden
        #   jeśli tak:
        #       ostatni znak wariacji = pierwszy_znak
        #       for liczba in przedzial 2 do dlugosc:
        #           liczba = -liczba
        #           czy wariacja[liczba] == ostatni_znak:
        #               jeśli nie:
        #                   zwiększ wariacja[liczba] o jeden znak
        #                   break
        #               jeśli tak:
        #                   spróbuj:
        #                       ustaw wariacja[liczba] = pierwszy_znak
        #                       jesli wariacja[liczba-1] != ostatni znak:
        #                           zwieksz wariacja[liczba-1] o jeden znak
        #                           przerwij petle
        #                   jeśli IndexError:
        #                       dlugosc += 1
        #                       jeśli dlugosc > dlugosc_max:
        #                           zakoncz wszystko
        #                       jeśli nie:
        #                           wariacja = [znak[0] * dlugosc]

# TEST
znaki = list("abc")
for wariacja in wariacje((2, 3), znaki):
    print(wariacja)
