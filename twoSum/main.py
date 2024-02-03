
def solution(nums, target):
    # Dicionário para armazenar a diferença entre 2 números. 
    # utilizando a matemática a nosso favor obtemos: n1 + n2 = target
    # Essa equação é igual a: n1 = target - n2
    # Ou seja, armazenando cada número no dicionário (numero:indice) 
    # Conseguimos focar em qual valor estamos procurando
    # Fazemos a diferença entre o número atual
    # Caso ele já esteja no dicionário o problema chega ao fim
    # Se não adicionamos o número atual no dicionário
    dictDiference = {}
    # Para cada número na lista de numbers
    # Indice
    for number in range(len(nums)):
        # Diferença = target - n2
        diference = target - nums[number]
        # Se a diferença já estiver no dicionário
        if diference in dictDiference:
            # Retornamos o indice associado ao valor buscado (diferença), e o number (indice)
            return [dictDiference[diference], number]
        # Adicionamos o número:indice no dicionário
        dictDiference[nums[number]] = number
    # Caso não encontrarmos uma solução retornamos None
    return None

print(solution([1,2,3], 5))