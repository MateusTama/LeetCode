# Função que recebe um número inteiro e retorna um boolean informando se é um palindromo (121 = 121), (149 = 941)
def isPalindrome(x: int) -> bool:
    # Retorna True se o inteiro transformado em string ao contrário ([::-1]) for igual a string do inteiro
    return str(x)[::-1] == str(x)

print(isPalindrome(123))