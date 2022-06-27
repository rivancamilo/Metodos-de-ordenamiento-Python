##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##              FUNCIONES DE LOS METODOS DE ORDENAMIENTO
##***************************************************************************************
def insertion_sort(array):
    #ordenamiento insertion sort
    for index in range(1, len(array)):
        currentValue = array[index]
        currentPosition = index
        while currentPosition > 0 and array[currentPosition - 1] > currentValue:
            array[currentPosition] = array[currentPosition -1]
            currentPosition = currentPosition - 1
        array[currentPosition] = currentValue
        
def merge_sort(lista):
    #ordenamienot por mezcla
    if len(lista) > 1:
        medio = len(lista) // 2 
        izquierda = lista[:medio]
        derecha = lista[medio:]
        #print(izquierda, '*' * 5, derecha)

        # Llamada recursiva en cada mitad.
        merge_sort(izquierda)
        merge_sort(derecha)

        # Iteradores para recorrer las dos sublistas
        i = 0; j = 0
        # Iterador de la lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

        #print(f'izquierda {izquierda}, derecha {derecha}')
        #print(lista)
        #print('-' * 50)
    return lista;      
 
def burbuja(arreglo):
    # Calculamos la longitud del arreglo para tener un código más limpio
    longitud = len(arreglo)
    # Recorremos todo el arreglo
    for i in range(longitud):
        # Dentro del ciclo, volvemos a recorrerlo. Pero ahora hasta el penúltimo elemento
        for indice_actual in range(longitud - 1):
            indice_siguiente_elemento = indice_actual + 1
            # Si el actual es mayor que el siguiente, ...
            # Nota: para un orden inverso, cambia `>` por `<`
            if arreglo[indice_actual] > arreglo[indice_siguiente_elemento]:
                # ... intercambiamos los elementos
                arreglo[indice_siguiente_elemento], arreglo[indice_actual] = arreglo[indice_actual], arreglo[indice_siguiente_elemento]
    # No hace falta regresar nada, pues el arreglo ya fue modificado
