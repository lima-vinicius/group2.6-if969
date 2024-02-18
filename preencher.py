import classes as cs
import csv

def vertice():
    v = cs.Vertices()
    with open('arquivoestacoes.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            origem, destino, distancia = linha[0], linha[1], linha[2]
            if origem not in v.estacao:
                v.estacao.append(origem)
            if destino not in v.estacao:
                v.estacao.append(destino)
            v.caminhos.append([origem,destino,float(distancia)])
    return v
