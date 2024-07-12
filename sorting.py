# ----------------
# Fonctions d'aide
# ----------------
def swap(tab, i, j):
    """Échange la place de deux éléments dans un tableau"""
    tab[i],tab[j]=tab[j],tab[i]


# ---------------
# Tris classiques
# ---------------
def bubble_sort(tab):
    """Trie le tableau en déplaçant les plus grosses valeurs vers la fin du
    tableau, un peu comme des bulles dans l'eau qui remonteraient à la
    surface"""
    n=len(tab)
    swapped=False
    for i in range(n-1):
        swapped=True
        for j in range(0, n-i-1):
        #j= i +1
            if tab[j] > tab[j+1]:
                tab[j],tab[j+1]=tab[j+1],tab[j]
    if not swapped:
        return
    #raise NotImplementedError
    return tab


def insertion_sort(tab):
    """Trie le tableau en plaçant l'élément courant à la bonne place dans
    le sous-tableau déjà trié"""
    for i in range(1,len(tab)):
        j=i
        index=tab[i]
        while j>0 and tab[j-1]>index:
            tab[j]=tab[j-1]
            j -=1
        tab[j]=index

    return tab


def selection_sort(tab):
    """Trie le tableau en cherchant le plus petit élément à mettre dans la
    première case, puis le second plus petit à mettre dans la seconde case,
    etc"""
    n=len(tab)
    for i in range(0,n-1):
        min=i
        for j in range(i+1,n):
            if tab[j]<tab[min]:
                min=j
        if min != i:
            #swap(A,i,min)
            (tab[i],tab[min])=(tab[min],tab[i])
    return tab



# --------------
# Tris récursifs
# --------------
def merge_sort(tab):
    """Trie le tableau via le principe de « diviser pour mieux régner »
    avec l'intelligence du tri qui se trouve au moment de la fusion"""
    merge_sort_r(tab, 0, len(tab))

def merge_sort_r(tab, start, end):
    if start<end-1:
        m=(start+end)//2
        merge_sort_r(tab,start,m)
        merge_sort_r(tab,m,end)
        merge(tab,start,m, end)
    #raise NotImplementedError

def merge(tab, start, middle, end):
    i=start
    j=middle
    temp=[0]*int(len(tab))
    for k in range(start, end):
        if i<middle and j<end:
            if tab[i]<=tab[j]:
                temp[k]=tab[i]
                #i=i+1
                i+=1
            else:
                temp[k]=tab[j]
                #j=j+1
                j+=1
        else:
            if i<middle:
                temp[k]=tab[i]
                i+=1
            else:
                temp[k]=tab[j]
                j+=1
    
    for k in range (start,end):
        tab[k]=temp[k]


def quick_sort(tab):
    """Divise le tableau en deux, trie chacune des sous-parties et fusionne
    intelligemment les deux sous-parties triées. L'intelligence se trouve
    dans la division du tableau."""

    quick_sort_r(tab, 0, len(tab)-1)

def quick_sort_r(tab, first, last):
    if first<last:
        pivot=partition(tab,first,last)
        quick_sort_r(tab, first, pivot-1)
        quick_sort_r(tab, pivot+1,last)

        
def partition(tab, first, last):
    pivot=tab[first]
    i=first
    j=last
    while i<=j:
        if tab[i]<=pivot:
            i=i+1
        else:
            if tab[j]>pivot:
                j-=1
            else:
                swap(tab,i,j)
    tab[first],tab[j]=tab[j],tab[first]
    return j
