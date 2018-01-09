from itertools import permutations
def generate_neighbourhood(initial,size):
    l=[]
    perms=permutations(initial[::-1])
    for i in range(size):
        l.append(list(perms.next())[::-1])
    return l


def is_tabu(tabu_list,candidate,n):
    for i in tabu_list:
        if i[n:]==candidate[n:]:
            return True
    return False
