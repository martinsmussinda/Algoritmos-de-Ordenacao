Entendi. Sem `main.py`. Cada arquivo roda sozinho, com a lista fixa e prints de execução na tela.

*Lista fixa pra todos:* `[19][7][20][6][15][10][16][13][11][8][6][5]`

1. bubble_sort.py
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
2. selection_sort.py
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
3. insertion_sort.py
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
4. merge_sort.py
import time

LISTA = [19, 7, 20, 6, 15, 10, 16, 13, 11, 8, 6, 5]

def merge_sort(arr):
    comp = trocas = [0, 0]
    print(f"Entrada: {arr}")

    def _merge(a):
        if len(a) > 1:
            mid = len(a)//2
            L, R = a[:mid], a[mid:]
            _merge(L); _merge(R)
            i=j=k=0
            while i < len(L) and j < len(R):
                comp[0] += 1
                if L[i] <= R[j]:
                    a[k] = L[i]; i += 1
                else:
                    a[k] = R[j]; j += 1
                k += 1; trocas[0] += 1
            while i < len(L):
                a[k] = L[i]; i+=1; k+=1; trocas[0]+=1
            while j < len(R):
                a[k] = R[j]; j+=1; k+=1; trocas[0]+=1
            print(f"Merge: {a}")
        return a

    _merge(arr)
    return arr, comp[0], trocas[0]

if __name__ == "__main__":
    inicio = time.perf_counter()
    arr = LISTA.copy()
    resultado, comp, trocas = merge_sort(arr)
    tempo = (time.perf_counter() - inicio) * 1000

    print(f"\n**Merge Sort**")
    print(f"Saída: {resultado}")
    print(f"Comparações: {comp} | Moves: {trocas} | Tempo: {tempo:.3f}ms")
5. heap_sort.py
import time

LISTA = [19, 7, 20, 6, 15, 10, 16, 13, 11, 8, 6, 5]

def heap_sort(arr):
    comp = trocas = 0
    print(f"Entrada: {arr}")

    def heapify(n, i):
        nonlocal comp, trocas
        largest = i
        l, r = 2*i+1, 2*i+2
        if l < n:
            comp += 1
            if arr[l] > arr[largest]: largest = l
        if r < n:
            comp += 1
            if arr[r] > arr[largest]: largest = r
        if largest!= i:
            arr[i], arr[largest] = arr[largest], arr[i]
            trocas += 1
            heapify(n, largest)

    n = len(arr)
    for i in range(n//2-1, -1, -1): heapify(n, i)
    print(f"Heap formado: {arr}")

    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        trocas += 1
        heapify(i, 0)
        print(f"Extrai maior: {arr}")
    return arr, comp, trocas

if __name__ == "__main__":
    inicio = time.perf_counter()
    arr = LISTA.copy()
    resultado, comp, trocas = heap_sort(arr)
    tempo = (time.perf_counter() - inicio) * 1000

    print(f"\n**Heap Sort**")
    print(f"Saída: {resultado}")
    print(f"Comparações: {comp} | Trocas: {trocas} | Tempo: {tempo:.3f}ms")
6. quick_sort.py
import time

LISTA = [19, 7, 20, 6, 15, 10, 16, 13, 11, 8, 6, 5]

def quick_sort(arr):
    comp = trocas = [0, 0]
    print(f"Entrada: {arr}")

    def _quick(a):
        if len(a) <= 1: return a
        pivot = a[len(a)//2]
        left, mid, right = [], []
        for x in a:
            comp[0] += 1
            if x < pivot: left.append(x)
            elif x == pivot: mid.append(x)
            else: right.append(x)
        trocas[0] += len(a)
        res = _quick(left) + mid + _quick(right)
        print(f"Partição pivô {pivot}: {res}")
        return res

    return _quick(arr), comp[0], trocas[0]

if __name__ == "__main__":
    inicio = time.perf_counter()
    arr = LISTA.copy()
    resultado, comp, trocas = quick_sort(arr)
    tempo = (time.perf_counter() - inicio) * 1000

    print(f"\n**Quick Sort**")
    print(f"Saída: {resultado}")
    print(f"Comparações: {comp} | Moves: {trocas} | Tempo: {tempo:.3f}ms")
Cada arquivo é independente. Roda com `python bubble_sort.py`, `python selection_sort.py`, etc.

Os prints mostram: lista inicial, cada troca/passo, e no final o resumo com comparações, trocas e tempo.

Quer que eu tire os prints de passo a passo e deixe só o resumo final?