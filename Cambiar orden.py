def swap(lista):
    if isinstance(lista,list)and(len(lista)%2==0):
        return swap_aux(lista)
    else: return "Error"
def swap_aux(lista):
    if lista==[]:
        return []
    else: return [lista[1],lista[0]]+swap_aux(lista[2:])
