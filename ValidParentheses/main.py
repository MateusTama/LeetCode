class Solution:
    def isValid(self, s: str) -> bool:
        # Se o número de elementos da string for par o programa é rodado
        if(len(s) % 2 == 0):
            # "Pilha"
            stack = []
            # String de fechamento associado a respectiva abertura
            closeToOpen = {")": "(", "}": "{", "]":"["}
            # Para cada caracter na string
            for caracter in s:
                # Se o caracter estiver no dict, ou seja, se for uma string de fechamento (")","}","]")
                if caracter in closeToOpen:
                    # if stack == True and stack[-1] == string de abertura
                    # Se a pilha for verdadeira (não pode ser vazia), e se o último caractere da pilha for a string de abertura associada ao caractere de fechamento atual
                    if stack and stack[-1] == closeToOpen[caracter]:
                        # Removemos a string de abertura da lista
                        stack.pop()
                    # Se tiver uma string de fechamento sem uma string de abertura
                    else:
                        return False
                # Se não for string de fechamento
                else:
                    stack.append(caracter)

            # Retornar True se a pilha estiver vazia, se não retornar False
            return True if not stack else False

        # Se o número de elementos for ímpar é retornado False, pois os fechamentos operam em pares
        else:
            return False

print(Solution().isValid('({})'))