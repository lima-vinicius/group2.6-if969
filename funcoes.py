def relaxar(p, u, v, w, pred):
    if p[v] > p[u] + w:
        pred[v] = u
        p[v] = p[u] + w

def rota(predecessor, peso, u, v):
    resultado = [v]
    ant = predecessor[v]

    pesofinal = [str(peso[v])]

    while ant != -1:
        resultado.append(ant)
        pesofinal.append(str(peso[ant]))
        ant = predecessor[ant]

    resultado = resultado[::-1]
    pesofinal = pesofinal[::-1]
    caminho = []
    x = " > ".join(resultado)

    for i in range(len(resultado) - 1):
        stringatual = f"De {resultado[i]} para {resultado[i + 1]} com a distância de {((float(pesofinal[i + 1]) - float(pesofinal[i]))):.1f} Km "
        caminho.append(stringatual)
    total = float(pesofinal[-1])
    stringatual = f"\nDistância total: {total:.2f} Km"
    caminho.append(stringatual)
    caminho.append(f"\nCaminho:\n{x}")
    stringfinal = "\n".join(caminho)

    print(stringfinal)