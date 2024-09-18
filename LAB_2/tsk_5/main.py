from classes import *


if __name__ == '__main__':
    

    # Создаем объекты РНК
    rna1 = RNA("AUGC")
    rna2 = RNA("CGGA")

    # Индексация
    print(rna1[0])  # A
    print(rna2[2])  # G

    # Склеивание РНК
    rna3 = rna1 + rna2
    print(rna3)  # AUGCCGGA

    # Перемножение РНК
    rna4 = rna1 * rna2
    print(rna4)  # Случайная последовательность, например: AGGC или CGGA

    # Конвертация РНК в ДНК
    dna1 = rna1.to_dna()
    print(dna1)  # Первая цепь: TACC Вторая цепь: ATGG

    # Создаем объекты ДНК
    dna2 = DNA("ATGC", "TACG")
    dna3 = DNA("GGCC", "CCGG")

    # Индексация ДНК
    print(dna2[0])  # ('A', 'T')
    print(dna3[1])  # ('G', 'C')

    # Склеивание ДНК
    dna4 = dna2 + dna3
    print(dna4)  # Первая цепь: ATGCGGCC Вторая цепь: TACGCCGG

    # Перемножение ДНК
    dna5 = dna2 * dna3
    print(dna5)  # Случайная последовательность

    # Проверка на равенство
    print(rna1 == rna2)  # False
    print(dna2 == DNA("ATGC", "TACG"))  # True