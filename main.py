cisla = [5, 2, 4, 1]  # Vytvoříme seznam čísel, která chceme seřadit.

def bubblesort(arr):  # Vytvoříme funkci bubblesort, která přijímá seznam arr.
    n = len(arr)  # Zjistíme počet prvků v seznamu a uložíme ho do proměnné n.

    for i in range(0, n - 1):  # První cyklus určuje počet průchodů seznamem.
        vymena = False  # Nastavíme, že zatím neproběhla žádná výměna.

        for j in range(0, n - i - 1):  # Druhý cyklus prochází seznam a porovnává sousední čísla.

            if cisla[j] > cisla[j + 1]:  # Zkontrolujeme, jestli je aktuální číslo větší než následující.

                pomocna = cisla[j]  # Uložíme si první číslo do pomocné proměnné.

                cisla[j] = cisla[j + 1]  # Na jeho místo přesuneme následující číslo.

                cisla[j + 1] = pomocna  # Na druhé místo vložíme původní číslo z pomocné proměnné.

                print(cisla)  # Vypíšeme seznam po provedené výměně.

    return print(cisla)  # Vypíšeme konečný seřazený seznam.

bubblesort(cisla)  # Zavoláme funkci a předáme jí seznam cisla.