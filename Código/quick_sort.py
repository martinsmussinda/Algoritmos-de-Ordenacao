import time

LISTA = [19, 7, 20, 6, 15, 10, 16, 13, 11, 8, 6, 5]

def quick_sort(arr):
    comp = [0]
    trocas = [0]
    print(f"Entrada: {arr}")

    def _quick(a):
        if len(a) <= 1: return a
        pivot = a[len(a)//2]
        left, mid, right = [], [], []
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