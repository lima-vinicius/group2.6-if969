# Definição das funções utilizadas pelo algoritmo de Bellman-Ford
def relaxar(pesos, u, v, w, predecessores):
    """
    Relaxa a aresta (u, v) se um caminho mais curto for encontrado de origem até v passando por u.
    Atualiza o vetor de predecessores e o vetor de pesos.
    """
    if pesos[v] > pesos[u] + w:
        predecessores[v] = u
        pesos[v] = pesos[u] + w

def calcular_rota(predecessores, pesos, origem, destino):
    """
    Retorna a rota mais curta entre os vértices origem e destino, junto com os pesos das arestas.
    """
    rota = [destino]
    antecessor = predecessores[destino]
    distancias = [pesos[destino]]

    while antecessor != -1:
        rota.append(antecessor)
        distancias.append(pesos[antecessor])
        antecessor = predecessores[antecessor]

    rota = rota[::-1]
    distancias = distancias[::-1]
    caminho = []

    caminho.append(f"Para chegar mais rápido da Estação {origem} até a Estação {destino}, siga este caminho:\n{' > '.join(rota)}\n")

    for i in range(len(rota) - 1):
        caminho.append(f"De {rota[i]} para {rota[i + 1]}, você irá percorrer {distancias[i + 1] - distancias[i]:.1f} Km")

    distancia_total = distancias[-1]
    caminho.append(f"\nDistância total percorrida da Estação {origem} até a Estação {destino}: {distancia_total:.2f} Km")

    return "\n".join(caminho)
