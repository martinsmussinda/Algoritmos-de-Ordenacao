import time

LISTA = [19, 7, 20, 6, 15, 10, 16, 13, 11, 8, 6, 5]

def bubble_sort(arr):
    comp = trocas = 0
    n = len(arr)
    print(f"Entrada: {arr}")

    for i in range(n):
        for j in range(0, n-i-1):
            comp += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                trocas += 1
                print(f"Troca {trocas}: {arr}")
    return arr, comp, trocas

if __name__ == "__main__":
    inicio = time.perf_counter()
    arr = LISTA.copy()
    resultado, comp, trocas = bubble_sort(arr)
    tempo = (time.perf_counter() - inicio) * 1000

    print(f"\n**Bubble Sort**")
    print(f"Saída: {resultado}")
    print(f"Comparações: {comp} | Trocas: {trocas} | Tempo: {tempo:.3f}ms")