def simcheck(lista,listb):
    sims=[]
    for i in range(len(lista)):
        for p in range(len(listb)):
            if listb[p]==lista[i]:
                sims.append(int(listb[p]))

    sims=list(dict.fromkeys(sims))
    return (sims)

list1 =  (input('List 1: '))
List1 = (list1.split(' '))
list2 = (input('list 2: '))
List2 = (list2.split(' '))
print(f'Output: {simcheck(List1,List2)}')