def my_max(l):
    # Sjekker om listen er tom
    if not l:
        raise ValueError("ikke definert for tomme lister")
    
    # hvis det bare er ett element, returner det
    if len(l) == 1:
        return l[0]
    
    # Rekursivt finner max mellom
    #det første elementet og max av resten
    return max(l[0], my_max(l[1:]))
print(my_max([5, 4, 3, 2, 1])) 
