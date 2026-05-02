import numpy as np
import matplotlib.pyplot as plt
import random

def calcular_distancia_euclidiana(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calcular_custo_total(solucao, matriz_distancias):
    return sum(matriz_distancias[solucao[i], solucao[i + 1]] for i in range(len(solucao) - 1))

def heuristica_caixeiro_guloso(n_cidades, matriz_distancias):
    visitadas = [False] * n_cidades
    solucao = [0]
    visitadas[0] = True

    for _ in range(1, n_cidades):
        ultima_cidade = solucao[-1]
        menor_distancia = float('inf')
        proxima_cidade = -1

        for i in range(n_cidades):
            if not visitadas[i] and matriz_distancias[ultima_cidade, i] < menor_distancia:
                menor_distancia = matriz_distancias[ultima_cidade, i]
                proxima_cidade = i

        solucao.append(proxima_cidade)
        visitadas[proxima_cidade] = True

    solucao.append(0)
    return solucao

def heuristica_insercao_aleatoria(n_cidades, matriz_distancias):
    solucao = [0]
    restantes = list(range(1, n_cidades))
    random.shuffle(restantes)

    for cidade in restantes:
        melhor_posicao = 0
        menor_custo = float('inf')

        for i in range(len(solucao)):
            nova_solucao = solucao[:i] + [cidade] + solucao[i:]
            custo = calcular_custo_total(nova_solucao + [0], matriz_distancias)
            if custo < menor_custo:
                menor_custo = custo
                melhor_posicao = i

        solucao.insert(melhor_posicao, cidade)

    solucao.append(0)
    return solucao

def aplicar_3opt(solucao, matriz_distancias):
    n = len(solucao) - 1
    melhoria = True

    while melhoria:
        melhoria = False
        for i in range(1, n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    reconexoes = [
                        solucao[:i + 1] + solucao[i + 1:j + 1] + solucao[j + 1:k + 1] + solucao[k + 1:],
                        solucao[:i + 1] + solucao[j + 1:k + 1] + solucao[i + 1:j + 1] + solucao[k + 1:],
                        solucao[:i + 1] + solucao[j + 1:k + 1] + solucao[i + 1:j + 1][::-1] + solucao[k + 1:],
                        solucao[:i + 1] + solucao[i + 1:j + 1][::-1] + solucao[j + 1:k + 1] + solucao[k + 1:],
                        solucao[:i + 1] + solucao[j + 1:k + 1][::-1] + solucao[i + 1:j + 1] + solucao[k + 1:],
                    ]

                    for nova_solucao in reconexoes:
                        custo_atual = calcular_custo_total(solucao, matriz_distancias)
                        novo_custo = calcular_custo_total(nova_solucao, matriz_distancias)

                        if novo_custo < custo_atual:
                            solucao = nova_solucao
                            melhoria = True
                            break
    return solucao

def ler_dados_tsp(arquivo):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()

    n_cidades = int(linhas[0].strip())
    ids, X, Y = [], [], []

    for linha in linhas[1:]:
        partes = linha.split()
        ids.append(int(partes[0]) - 1)
        X.append(float(partes[1]))
        Y.append(float(partes[2]))

    return n_cidades, np.array(ids), np.array(X), np.array(Y)

def construir_matriz_distancias(n, X, Y):
    matriz = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            matriz[i, j] = calcular_distancia_euclidiana(X[i], Y[i], X[j], Y[j])
    return matriz

def plotar_solucao(X, Y, solucao, custo):
    plt.figure(figsize=(8, 6))
    plt.scatter(X, Y, color='blue', label='Cidades')

    for i in range(len(X)):
        plt.text(X[i] + 0.1, Y[i], f'{i}', fontsize=8)

    for i in range(len(solucao) - 1):
        plt.plot(
            [X[solucao[i]], X[solucao[i + 1]]],
            [Y[solucao[i]], Y[solucao[i + 1]]],
            color='green'
        )

    plt.title(f'Solução TSP - Custo: {custo:.2f}')
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    filename = 'TSP_n50_2.txt'

    n_cidades, ids, X, Y = ler_dados_tsp(filename)
    matriz_distancias = construir_matriz_distancias(n_cidades, X, Y)

    # Geração de soluções iniciais
    solucoes_iniciais = [
        heuristica_caixeiro_guloso(n_cidades, matriz_distancias),
        heuristica_insercao_aleatoria(n_cidades, matriz_distancias)
    ]

    melhores_resultados = []

    for solucao_inicial in solucoes_iniciais:
        custo_inicial = calcular_custo_total(solucao_inicial, matriz_distancias)
        print(f'Custo inicial: {custo_inicial:.2f}')

        # Aplicar o 3-opt
        solucao_otimizada = aplicar_3opt(solucao_inicial, matriz_distancias)
        custo_otimizado = calcular_custo_total(solucao_otimizada, matriz_distancias)

        print(f'Custo otimizado: {custo_otimizado:.2f}')
        melhores_resultados.append((solucao_otimizada, custo_otimizado))

    melhor_solucao, menor_custo = min(melhores_resultados, key=lambda x: x[1])
    print(f'Melhor solução encontrada - Custo: {menor_custo:.2f}')

    plotar_solucao(X, Y, melhor_solucao, menor_custo)
