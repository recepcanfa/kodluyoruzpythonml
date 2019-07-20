import itertools as it


def hesapla(g, M):
    toplam = sum(map(lambda x: x ** 2, g))
    return toplam % M

if __name__ == "__main__":
    k, m = map(int, input().split())
    N = []
    for _ in range(k):
        girdiler = list(map(int, input().split()))[1:]
        N.append(girdiler)
    print(max([hesapla(t,m) for t in it.product(*N)]))