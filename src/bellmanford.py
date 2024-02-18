# Implementação do algoritmo de Bellman-Ford
import funcoes as fc

def bellmanFord(origem, grafo, destino):
    """
    Executa o algoritmo de Bellman-Ford para encontrar o menor caminho entre origem e destino em um grafo.
    """
    # Inicializar vetores de pesos e predecessores
    predecessores = {}
    pesos = {}
    for estacao in grafo.estacoes:
        pesos[estacao] = float('inf')
        predecessores[estacao] = -1

    # A distância da origem para si mesma é zero
    pesos[origem] = 0

    # Relaxar todas as arestas repetidamente para encontrar o menor caminho
    for _ in range(len(grafo.estacoes) - 1):
        for u, v, w in grafo.caminhos:
            fc.relaxar(pesos, u, v, w, predecessores)

    # Verificar se há ciclos negativos
    for u, v, w in grafo.caminhos:
        if pesos[v] > pesos[u] + w:
            print('Ciclo negativo detectado')
            return "Ciclo negativo detectado"

    # Calcular e retornar a rota mais curta como uma string
    resultado = fc.calcular_rota(predecessores, pesos, origem, destino)
    return resultado
