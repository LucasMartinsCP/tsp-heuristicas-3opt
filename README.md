📚 Sobre o Projeto

Este projeto foi desenvolvido como parte da disciplina de Otimização, do curso de Ciência da Computação do IFPR – Campus Pinhais.

O trabalho tem como objetivo implementar e analisar abordagens heurísticas para a resolução do Problema do Caixeiro Viajante (TSP – Travelling Salesman Problem), um dos problemas clássicos da área de otimização combinatória.

🧠 Problema Abordado

O Problema do Caixeiro Viajante consiste em determinar a menor rota possível que permita a um viajante:

Visitar um conjunto de cidades exatamente uma vez
Retornar à cidade de origem
Minimizar a distância total percorrida

Por se tratar de um problema NP-difícil, soluções exatas tornam-se inviáveis para instâncias maiores, o que justifica o uso de heurísticas e métodos aproximados.

⚙️ Abordagem Utilizada

Neste trabalho, foi adotada uma estratégia em duas etapas:

🔹 1. Construção de Soluções Iniciais

Foram utilizadas duas heurísticas distintas:

Heurística do Vizinho Mais Próximo (Gulosa)
Constrói uma rota escolhendo sempre a cidade mais próxima ainda não visitada.
Heurística de Inserção Aleatória
Gera uma solução inicial mais diversificada, inserindo cidades em posições que minimizam o custo incremental.
🔹 2. Otimização com Busca Local (3-opt)

Após a geração das soluções iniciais, foi aplicado o algoritmo 3-opt, uma técnica de otimização local que:

Remove três arestas da rota atual
Reconecta os segmentos de diferentes formas
Aceita modificações que reduzem o custo total

Esse processo é repetido iterativamente até que não sejam encontradas melhorias adicionais.

📊 Objetivo do Trabalho

O foco principal do projeto é:

Comparar diferentes formas de construção de soluções iniciais
Avaliar o impacto da otimização local (3-opt) na qualidade das rotas
Demonstrar, na prática, a aplicação de técnicas heurísticas em problemas NP-difíceis
⚖️ Considerações sobre Desempenho

A implementação prioriza a qualidade das soluções em detrimento do tempo de execução.

O uso do algoritmo 3-opt, apesar de produzir resultados significativamente melhores, possui custo computacional elevado, especialmente para instâncias com maior número de cidades.

📈 Resultados

O sistema gera:

Custos das soluções iniciais
Custos após otimização
Comparação entre abordagens
Visualização gráfica da melhor rota encontrada
💡 Conclusão

Este projeto demonstra como a combinação de heurísticas construtivas com técnicas de busca local pode produzir soluções eficientes para problemas complexos, mesmo na ausência de algoritmos exatos viáveis.

Além disso, reforça a importância do equilíbrio entre qualidade da solução e custo computacional, um dos principais desafios na área de otimização.
