import functools
import operator

# power_set = [ [], [1], [2], [3], [1, 2], [1,3], [2,3], [1,2,3] ]

def power_set(array):
    if array == []:
        return [[]]


def alg_optimal_iterative(number, T):
    if(len(number) == 0):
        return []
    
    best_array = []
    best_total = 0

    for i in range(len(power_set)):
        current_set = power_set[i]

        current_set_sum = functools.reduce(operator.add, current_set)

        if(current_set_sum <= T and current_set_sum >= best_total):
            best_array = current_set
            best_total = current_set_sum


    
    return best_array

def alg_optimal_iterative2(number, T):
    if(len(number) == 0):
        return []
    
    best_array = []
    best_total = 0

    for i in range(len(power_set)):
        current_set = power_set[i]

        current_set_sum = functools.reduce(operator.add, current_set)

        if(current_set_sum <= T and current_set_sum >= best_total):
            best_array = current_set
            best_total = current_set_sum


    
    return best_array


def solution_10(number_list, T):
    if (T == 0 or number_list == []):
        return []
    
    first_element = number_list[0]

    first_solution = []

    if(first_element <= T):
        first_solution = solution_10(number_list[1:-1], T - first_element)

    second_solution = solution_10(number_list[1:-1], T)

    if sum(first_solution) + first_element < sum(second_solution):
        return second_solution
    elif sum(first_solution) + first_element <= T:
        return first_solution.append(first_element)
    else:
        return second_solution



alg_optimal_iterative(power_set, 3)