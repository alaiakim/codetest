def solution(sizes):
    garos = []
    seros = []
    for i in range(len(sizes)):
        garos.append(sizes[i][0])
        seros.append(sizes[i][1])
    garo = max(garos)
    for i in range(len(seros)):
        if seros[i] == max(seros):
            if garos[i] < seros[i] and garos[i] < garo:
                seros[i] = garos[i]
    sero = max(seros)
    return (garo * sero)

print (solution([[60, 50], [30, 70], [60, 30], [80, 40]]))