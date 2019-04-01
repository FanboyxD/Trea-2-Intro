def contar_consonantes(palabra):
    if isinstance(palabra,str):
        return consonantes_aux(palabra)
    else: return "error"
def consonantes_aux(palabra):
    if palabra == (""):
        return 0
    elif palabra[0]=="a":
        return consonantes_aux(palabra[1:])
    elif palabra[0]=="A":
        return consonantes_aux(palabra[1:])
    elif palabra[0]=="e":
        return consonantes_aux(palabra[1:])
    elif palabra[0]=="E":
        return consonantes_aux(palabra[1:])
    elif palabra[0]=="i":
        return consonantes_aux(palabra[1:])
    elif palabra[0]=="I":
        return consonantes_aux(palabra[1:])
    elif palabra[0]=="o":
        return consonantes_aux(palabra[1:])
    elif palabra[0]=="O":
        return consonantes_aux(palabra[1:])
    elif palabra[0]=="u":
        return consonantes_aux(palabra[1:])
    elif palabra[0]=="U":
        return consonantes_aux(palabra[1:])
    else:return 1 + consonantes_aux(palabra[1:])
