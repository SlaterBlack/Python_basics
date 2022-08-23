def join_n_sort(lista,listb):
    listout=[]
    for i in range(len(lista)):
        listout.append(int(lista[i]))
    for i in range(len(listb)):
        listout.append(int(listb[i]))
    listout.sort(reverse=True)
    print(listout)

list1 =  (input('List 1: '))
List1 = (list1.split(' '))
list2 = (input('list 2: '))
List2 = (list2.split(' '))
join_n_sort(List1,List2)