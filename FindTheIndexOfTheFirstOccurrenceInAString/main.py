# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Nova string modificável igual a string que armazena a palavra
        newString = haystack
        # Primeira letra da palavra procurada
        firstLetter = needle[0]
        # Loop Infinito (não sabemos quantas vezes repetiremos o código)
        while True:
            # Se a string a ser procurada estiver na nova string modificável executaremos o código, se não retornamos -1
            if (needle in newString):
                # Pegamos o índice da primeira letra a ser procurada na string modificável
                indexFirst = newString.index(firstLetter)
                # Se a palavra a ser procurada estiver no intervalo da primeira letra da palavra a ser procurada e o tamanho da string
                if (needle in newString[indexFirst:indexFirst+len(needle)]):
                    # Retornamos o tamanho da palavra original - o tamanho da string modificável + o indice da primeira letra
                    return (len(haystack) - len(newString)) + indexFirst
                # Se não retiramos a letra da nova string
                newString = newString[indexFirst+1::]
            else:
                return -1

print(Solution().strStr("mississippi", "ssip"))
