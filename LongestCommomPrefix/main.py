# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

# Recebe uma lista de strings
def longestCommonPrefix(strs) -> str:
    # Inicialindo a resposta
    res = ''
    # Para cada letra da primeira string
    for i in range(len(strs[0])):
        # Para cada string da lista de strings
        for s in strs:
            # Se o índice for igual ao tamanho da string ou se a letra da string for diferente da primeira string retornamos o resultado atual
            # 1. índice atual for do mesmo tamanho da string = Não a mais nada para ser verificado, retornamos o resultado (indice começa em 0)
            # 2. Se no mesmo indice as letras forem diferentes
            # Retornamos resultado atual/string vazia
            if (i == len(s) or s[i] != strs[0][i]):
                return res
        # Após rodas todas as strings com o mesmo índice (letra) adicionamos a letra a resposta
        res += strs[0][i]  
    # Se não cair no if retornamos o res (string iguais)
    return res

print(longestCommonPrefix(["ab", "a"]))
