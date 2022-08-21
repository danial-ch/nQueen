# danial chekani 9821023

import numpy as np
import math
from operator import itemgetter
import time

start_time = time.time()

# genetic configuration
cross_over_rate = 0.5
mutation_rate = 0.5
population = 1000
generations = 200
keep_percentage = 10
n = 8

def fitness_function(row):
    score = 0
    for i in range(n):
        for j in range(i,n):
            if i != j and (row[i] == row[j] or abs(i-j) == abs(row[i]-row[j])):
                score += 1
    return score

best_score = math.inf
best_solution = []

mul = int(100 / keep_percentage)

# initial population
pop = np.random.randint(1, 9 ,  size=(population , n ))

for i in range(generations):
    tmp = []
    for row in pop:
        score = fitness_function(row)
        if score < best_score:
            best_score = score
            best_solution = row
        if best_score == 0:
            break
        tmp.append([row,score])
    else:
        new_pop = []
        tmp = sorted(tmp, key=itemgetter(1))
        tmp = tmp[0:math.ceil(len(tmp)/mul):]
        pop = []
        top_res_size = math.ceil(len(tmp)/10)
        
        for j in range(0,len(tmp)):
            for k in range(mul):
                gen = tmp[j][0]
                gen = gen.copy()
                new_pop.append(gen)
        
        # mutation
        for j in range(top_res_size,len(new_pop)):
            if np.random.rand() < mutation_rate:
                mutated_gen = new_pop[j]
                mutated_gen[np.random.randint(0,8)] = np.random.randint(1,n + 1)
                new_pop[j] = mutated_gen

        # cross over
        size = len(new_pop)
        for j in range(top_res_size,size):
            for k in range(j+1,size):
                if np.random.rand() < cross_over_rate:
                    first_cross_over_gen = new_pop[j]
                    second_cross_over_gen = new_pop[size - k]
                    first_new_gen = np.concatenate([first_cross_over_gen[:int(n/2)], second_cross_over_gen[int(n/2):]])
                    second_new_gen = np.concatenate([second_cross_over_gen[:int(n/2)], first_cross_over_gen[int(n/2):]])
                    new_pop[j] = first_new_gen
                    new_pop[size - k] = second_new_gen
                    break

        for j in range(top_res_size):
            pop.append(tmp[j][0])
        for j in range(top_res_size,size):
            pop.append(new_pop[j])
        continue
    break

print('Best Solution: ', best_solution)
print("Exectution Time : ", round((time.time() - start_time),3), " seconds")