cisla = [5, 2, 4, 1]

def bubblesort(arr):
    n = len (arr)
    for i in range(0, n - 1):
        vymena = False
        for j in range(0, n - i - 1):
            if cisla [j] > cisla[j + 1]:
                pomocna = cisla[j]
                cisla[j] = cisla[j + 1]
                cisla[j + 1] = pomocna
                print(cisla)
    return print(cisla)

bubblesort(cisla)