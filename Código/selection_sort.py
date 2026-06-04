def selection_sort(vetor):
    n = len(vetor)

    for i in range(n):
        menor = i

        for j in range(i + 1, n):
            if vetor[j] < vetor[menor]:
                menor = j

        vetor[i], vetor[menor] = vetor[menor], vetor[i]

    return vetor
