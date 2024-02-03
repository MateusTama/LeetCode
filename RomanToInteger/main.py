# Algoritmo que converte de número romano para número inteiro
def romanToInt(s: str) -> int:
    # Dicionário com todos os números romanos associdos ao seu respectivo valor em inteiros
    roman = {"I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000}
    # Novo dicionário associando o indice da algarismo romano na string com a letra que este representa
    strRoman = {}
    # for para percorrer todas os algarismos romanos
    for indice in range(0, len(s)):
        # Armazenando a letra em uma variável (apenas para entendimento, não é necessário)
        letra = s[indice]
        # Associonando o indice a letra representada por este na str. /
        strRoman[indice] = letra
    # Declarando uma variável para ser usada no for
    resultado = 0
    # Iniciando com uma variável que vai armazenar a letra que veio antes da que está sendo utilizada no for
    lastValue = 0
    # Para cada ocorrência no dicionário
    for indice in strRoman:
        # Pegamos a letra associada ao indice
        letter = strRoman[indice]
        # Passamos a letra para pegar o valor que esta representa, utilizando o dicionário que contém estes valores
        value = roman[letter]
        # Se o último valor for menor que o atual (Os algarismos romanos estão em ordem). Exemplo (XIX)
        if lastValue < value:
            # Retiramos o valor adicionados anteriormente
            resultado = resultado - lastValue
            # Novo valor vai ser igual ao valor atual (maior) - o valor passado (menor)
            newValue = value - lastValue
            # Somamos o novo valor no resultado
            resultado += newValue
            # Atualizamos a variável do último valor
            lastValue = value
        # Se o valor atual for menor que o ultimo valor
        else:
            # Atualizamos o last value
            lastValue = value 
            # Somamos no resultado o valor associada a letra no dicionário que armazena os valores de cada letra dos algarismos romanos
            resultado += roman[strRoman[indice]]
    # Retornamos o resultado
    return resultado
            
# OBS: Existem inúmeras outras maneiras de resolver esse desafio.
print(romanToInt("MIII"))