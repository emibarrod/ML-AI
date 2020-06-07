def pasarAMatriz(arrayDeImagen):
    """
    El objetivo de esta función es poder meter los array de nuestro
    X_test en el método plt.matshow() ya que no acepta arrays unidimensionales.
    
    Recibe: un array con los píxeles de una imagen
    Devuelve: Una matriz 8x8 con los píxeles de la matriz
    """
    cont = 0
    lista_final = []
    lista_temp = []
    for i in arrayDeImagen:
        if cont in [0,1]:
            lista_temp.append(i)
        elif cont%7  == 0:
            lista_temp.append(i)
            lista_final.append(lista_temp)
            lista_temp = []
            cont=-1
        else:
            lista_temp.append(i)
    
        cont+=1
    return lista_final    
