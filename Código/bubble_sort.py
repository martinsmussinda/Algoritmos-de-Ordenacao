def bubble_sort(vetor):
    n = len(vetor)

    for i in range(n):
        for j in range(0, n - i - 1):
            if vetor[j] > vetor[j + 1]:
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]

    return vetor
