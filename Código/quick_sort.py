def quick_sort(vetor):
    if len(vetor) <= 1:
        return vetor

    pivo = vetor[len(vetor) // 2]

    menores = [x for x in vetor if x < pivo]
    iguais = [x for x in vetor if x == pivo]
    maiores = [x for x in vetor if x > pivo]

    return quick_sort(menores) + iguais + quick_sort(maiores)