class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Tira os espaçamentos do início e do final
        s = s.strip()
        # Pega a lista de palavras utilizando o separador ' '
        substring = s.split()
        # Retorna o tamanho da última palavra da coleção de substrings 
        return len(substring[len(substring)-1])

print(Solution().lengthOfLastWord('  teste teste  '))