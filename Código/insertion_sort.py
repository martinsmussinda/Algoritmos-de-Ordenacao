def insertion_sort(vetor):
    for i in range(1, len(vetor)):
        chave = vetor[i]
        j = i - 1

        while j >= 0 and vetor[j] > chave:
            vetor[j + 1] = vetor[j]
            j -= 1

        vetor[j + 1] = chave

    return vetor
