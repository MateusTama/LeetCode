# Função que recebe um número inteiro e retorna um boolean informando se é um palindromo (121 = 121), (149 = 941)
def isPalindrome(x: int) -> bool:
    # Convertendo um número para string
    strNumber = str(x)
    # Iniciando variável palindromeNumber como str
    palindromeNumber = ""
    # Indice = número de algarismo do número
    indice = len(strNumber)
    # Rodando um for no mesmo número que algarismo
    for index in range(0, indice):
        # Adicionando o último algarismo do strNumber (0, 1, 2)
        palindromeNumber += strNumber[indice-1]
        # Mudando o valor do índice para adicionar todos os algarismos
        indice -= 1
    # Se o palindromeNumber == str(numero inteiro inicial)
    if palindromeNumber == str(x):
        # Retorna True
        return True
    # Se não retorna False
    return False

print(isPalindrome(121))