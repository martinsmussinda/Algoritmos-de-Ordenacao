import time

LISTA = [19, 7, 20, 6, 15, 10, 16, 13, 11, 8, 6, 5]

def shell_sort(arr):
    comp = trocas = 0
    n = len(arr)
    print(f"Entrada: {arr}")

    gap = n // 2
    while gap > 0:
        print(f"\nGap = {gap}")
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                comp += 1
                arr[j] = arr[j - gap] 
                trocas += 1
                j -= gap
            if j >= gap: comp += 1
            arr[j] = temp
            print(f"Insere {temp}: {arr}")
        gap //= 2

    return arr, comp, trocas

if __name__ == "__main__":
    inicio = time.perf_counter()
    arr = LISTA.copy()
    resultado, comp, trocas = shell_sort(arr)
    tempo = (time.perf_counter() - inicio) * 1000

    print(f"\n**Shell Sort**")
    print(f"Saída: {resultado}")
    print(f"Comparações: {comp} | Moves: {trocas} | Tempo: {tempo:.3f}ms")