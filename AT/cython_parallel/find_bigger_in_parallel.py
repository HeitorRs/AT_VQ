import numpy as np
from multiprocessing import Pool
from vector import vector_by_scalar

#Função que gera o vetor e executa o totalizador
def biggest_sums(scalar):
    vec = np.random.uniform(1, 100, 1000)

    modified_vec = vector_by_scalar(vec, scalar)

    total = np.sum(modified_vec)

    return total

#Função para encontrar o maior valor
def find_max_sum():
    escalares = [2, 3, 4, 5, 6, 7, 8, 9]

    with Pool(processes=8) as pool:
        results = pool.map(biggest_sums, escalares)

    max_sum = max(results)

    #Verificando qual escalar teve o maior resultado
    for i, result in enumerate(results):
        if result == max_sum:
            print(f"Escalar {escalares[i]} gerou o maior valor total: {max_sum}")
            return max_sum

    return 0.0

if __name__ == "__main__":
    find_max_sum()
