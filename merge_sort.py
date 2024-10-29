

def merge_sort(array):

    # divisão de array
    if len(array) > 1:
        divisao = len(array) // 2
        esquerda =  array[:divisao]
        direita = array[divisao:]

        merge_sort(direita)
        merge_sort(esquerda)

        i=j=k=0


     # Ordena esquerda e direita
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                array[k] = esquerda[i]
                i += 1
            
            else:
                array[k] = direita[j]
                j += 1
            k +=1

      # ordenação final
        while i < len(esquerda):
            array[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            array[k] = direita[j]
            j += 1
            k += 1
        
        return array
    
  
print(merge_sort([38,27,43,3,9,82,10] ))
