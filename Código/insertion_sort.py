import time

LISTA = [19, 7, 20, 6, 15, 10, 16, 13, 11, 8, 6, 5]

def insertion_sort(arr):
    comp = trocas = 0
    print(f"Entrada: {arr}")

    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            comp += 1
            arr[j+1] = arr[j]
            trocas += 1
            j -= 1
        if j >= 0: comp += 1
        arr[j+1] = key
        print(f"Insere {key}: {arr}")
    return arr, comp, trocas

if __name__ == "__main__":
    inicio = time.perf_counter()
    arr = LISTA.copy()
    resultado, comp, trocas = insertion_sort(arr)
    tempo = (time.perf_counter() - inicio) * 1000

    print(f"\n**Insertion Sort**")
    print(f"Saída: {resultado}")
    print(f"Comparações: {comp} | Moves: {trocas} | Tempo: {tempo:.3f}ms")
