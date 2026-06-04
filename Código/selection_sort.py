import time

LISTA = [19, 7, 20, 6, 15, 10, 16, 13, 11, 8, 6, 5]

def selection_sort(arr):
    comp = trocas = 0
    print(f"Entrada: {arr}")

    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            comp += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx!= i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            trocas += 1
            print(f"Troca {trocas}: {arr}")
    return arr, comp, trocas

if __name__ == "__main__":
    inicio = time.perf_counter()
    arr = LISTA.copy()
    resultado, comp, trocas = selection_sort(arr)
    tempo = (time.perf_counter() - inicio) * 1000

    print(f"\n**Selection Sort**")
    print(f"Saída: {resultado}")
    print(f"Comparações: {comp} | Trocas: {trocas} | Tempo: {tempo:.3f}ms")
