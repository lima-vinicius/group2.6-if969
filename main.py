import preencher as pc
import bellmanford as bf

v = pc.vertice()
origem = input('Digite a Estação de origem: ')
destino = input('Digite a Estação final: ')
if origem not in v.estacao or destino not in v.estacao:
    print('Estação não encontrada.')
else:
    bf.bellmanford(origem, v, destino)