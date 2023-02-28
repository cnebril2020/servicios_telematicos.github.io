## variables mutables: drop, append, etc. --> listas
## variables inmutables: variables normales

f = open("nombrefichero.txt", "a") # "rb" --> lectura binaria, "r+" --> lectura y escritura, "w" --> sobreescribe, "a" --> añade una nueva linea
#cadena = f.read()  # f.read(5) --> lee 5 linas del fichero
"""listaCadenas = f.readlines()
for e in listaCadenas:
    print(e, end="")
"""
f.write("\nCadena nueva de texto") # se sobreescibre
f.close()