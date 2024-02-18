import funcoes as fc

def bellmanford(origem, grafo, destino):
    pred = {}
    p = {}
    for i in grafo.estacao:
        p[i] = float('inf')
        pred[i] = -1

    p[origem] = 0

    for i in range(len(grafo.estacao) - 1):
        for u, v, w in grafo.caminhos:
            fc.relaxar(p, u, v, w, pred)

    for u, v, w in grafo.caminhos:
        if p[v] > p[u] + w:
            print('Ciclo negativo detectado')
            return

    fc.rota(pred, p, origem, destino)

    return True