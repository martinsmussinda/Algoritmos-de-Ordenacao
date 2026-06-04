def shell_sort(vetor):
    n = len(vetor)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = vetor[i]
            j = i

            while j >= gap and vetor[j - gap] > temp:
                vetor[j] = vetor[j - gap]
                j -= gap

            vetor[j] = temp

        gap //= 2

    return vetor
