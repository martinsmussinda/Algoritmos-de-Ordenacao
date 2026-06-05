import random
import time

#LISTA = [random.randint(1, 20) for _ in range(10)]
#LISTA = [random.randint(1, 20) for _ in range(100)]
#LISTA = [random.randint(1, 20) for _ in range(1000)]

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
    print(f"\nLista original: {LISTA}")
    print(f"\nSaída: {resultado}")
    print(f"\nComparações: {comp} | Movimentos: {trocas} | Tempo: {tempo:.3f}ms")